import json
import csv

emo = ['neutral', 'happy', 'sad', 'surprise', 'anger', 'fear']

for idx, i in enumerate(emo):
    with open(f"./data/{i}/img_emotion_sample_data({i}).json", "r") as f:
        data = json.load(f)
    with open('fer.csv', 'w') as c:
        wr = csv.writer(c)
        for id, d in enumerate(data):
            wr.writerow([id, 'train', f"./datasets/{i}/{data[idx]['filename']}", idx])
