import face_recognition_knn as fkn
import cv2
import face_recognition
import pickle
import requests
from file_system import data


def finish_registraion():
    knn_clf = fkn.train('./train_dir', verbose=True)
    video_capture = cv2.VideoCapture(0)
    while True:
        data_prev = data.copy()
        ret, frame = video_capture.read()
        cv2.imwrite('res.png', frame)
        res = fkn.predict('res.png', knn_clf=knn_clf)
        data[res[0]] = True
        if data != data_prev:
            requests.post('http://localhost:5000/admin', json=data)


# finish_registraion()
