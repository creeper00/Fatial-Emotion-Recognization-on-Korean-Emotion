from fer import FER
import cv2
from os import walk
import numpy as np

emo = ['neutral', 'happy', 'sad', 'surprise', 'anger', 'fear']
total=0
correct=0
detector = FER()
for i in emo:
    filenames = next(walk(f'./datasets/{i}/'), (None, None, []))[2]
    for j in filenames:
        path = f"./datasets/{i}/{j}"
        img_array = np.fromfile(path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        label, score = detector.top_emotion(img)
        if label==i : correct+=1
        total+=1
    print(i)

print((correct*100)/total)