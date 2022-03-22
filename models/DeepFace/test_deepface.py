import cv2
from deepface import DeepFace
import numpy as np
from os import walk

emo = ['neutral', 'happy', 'sad', 'surprise', 'anger', 'fear']
total=0
correct=0
for i in emo:
    filenames = next(walk(f'../../datasets/{i}/'), (None, None, []))[2]
    for j in filenames:
        try:
            path = f"../../datasets/{i}/{j}"
            img_array = np.fromfile(path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            label = DeepFace.analyze(img,actions=['emotion'])['dominant_emotion']
            if label==i : correct+=1
            total+=1
        except:
            continue
    print(i)

print((correct*100)/total)