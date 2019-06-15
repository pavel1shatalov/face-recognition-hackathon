import face_recognition_knn as fkn
import cv2
import face_recognition


def finish_registraion():
    video_capture = cv2.VideoCapture(0)
    fkn.train('./train_dir', model_save_path='faces_prediction_model.pckl', verbose=True)
    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        print(fkn.predict(None, face_locations, face_recognition, model_path='faces_prediction_model.pckl'))
