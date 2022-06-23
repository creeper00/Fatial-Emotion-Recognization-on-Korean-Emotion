# FER on Korean Emotion

FER model tuned with Korean Emotion dataset  
Classify emotions into 3 labels: Angry/sad, Happy, Suprise  
  
<img width="271" alt="image" src="https://user-images.githubusercontent.com/43807159/175269047-15e00c66-8633-49ff-91b4-f93d2d77193f.png">


### Backend
`finetuned_model.h5` : trained model  
`project.ipynb` : backend server & training code  
`base_models` : model test results

### Frontend
vue code for result visualization
1. run backend server in colab
2. set new ip address(colab backend server) to vue websocket config
3. run frontend
4. copy-paste youtube url to frontend form
5. watch analysis (you should refresh page for next analysis)


### Dataset
- https://aihub.or.kr/aidata/27716

### Reference
- https://github.com/yaoing/DAN
- https://github.com/serengil/deepface
- https://github.com/justinshenk/fer
- https://github.com/oarriaga/face_classification
