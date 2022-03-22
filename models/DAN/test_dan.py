import os
import argparse
from os import walk

from PIL import Image

import torch
from torchvision import transforms

from networks.dan import DAN

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help='Image file for evaluation.')
 
    return parser.parse_args()

class Model():
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.data_transforms = transforms.Compose([
                                    transforms.Resize((224, 224)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
                                ])
        self.labels = ['neutral', 'happy', 'sad', 'surprise', 'fear', 'disgust', 'anger']

        self.model = DAN(num_head=4, num_class=7, pretrained=False)
        checkpoint = torch.load('./affecnet7_epoch6_acc0.6569.pth',
            map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'],strict=True)
        self.model.to(self.device)
        self.model.eval()
    
    def fit(self, path):
        img = Image.open(path).convert('RGB')
        img = self.data_transforms(img)
        img = img.view(1,3,224,224)
        img = img.to(self.device)

        with torch.set_grad_enabled(False):
            out, _, _ = self.model(img)
            _, pred = torch.max(out,1)
            index = int(pred)
            label = self.labels[index]

            return index, label

if __name__ == "__main__":
    args = parse_args()

    model = Model()

    emo = ['neutral', 'happy', 'sad', 'surprise', 'anger', 'fear']
    total=0
    correct=0
    for i in emo:
        filenames = next(walk(f'../../datasets/{i}/'), (None, None, []))[2]
        for j in filenames:
            image = f"../../datasets/{i}/{j}"

            index, label = model.fit(image)
            if label==i : correct+=1
            total+=1

    print((correct*100)/total)