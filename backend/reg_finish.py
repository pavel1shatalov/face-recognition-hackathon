import face_recognition_knn as fkn
import cv2
import face_recognition
import pickle


def finish_registraion():
    knn_clf = fkn.train('./train_dir', model_save_path='faces_prediction_model.pckl', verbose=True)
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        cv2.imwrite('res.png', frame)
        res = fkn.predict('res.png', knn_clf=knn_clf)
        for name, (top, right, bottom, left) in res:
            print("- Found {} at ({}, {})".format(name, left, top))


finish_registraion()
