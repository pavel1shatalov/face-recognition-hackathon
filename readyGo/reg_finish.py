import face_recognition_knn as fkn
import cv2
import face_recognition
import pickle
import requests
from file_system import data
import json

def finish_registraion():
    print('Ready')
    video_capture = cv2.VideoCapture(0)
    data_prev = data.copy()
    ret, frame = video_capture.read()
    cv2.imwrite('res.png', frame)
    res = fkn.predict('res.png', model_path='faces_prediction_model.pckl')
    if not res:
        print("FAIDED TO RECOGNIZE")
        return
    print(res)
    print(data)
    # for user_tup in res:
    #     name = user_tup[0]
    #     if name == 'unknown':
    #         continue
    #     user_dict = next((item for item in data if item['name'] == name), False)
    #     if user_dict:
    #         user_dict['available'] = 1
    #     else:
    #         user_dict['available'] = 0
    for user_dict in data:
        table = set(item[0] for item in res)
        if user_dict['name'] in table:
            user_dict['available'] = 1
        else:
            user_dict['available'] = 0
    video_capture.release()