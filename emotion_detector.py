import cv2
import numpy as np
from keras.models import load_model
from helpers import *


class EmotionDetector():
    def __init__(self, **kwargs):
        self.subscribers = []
        self.emotion_offsets = kwargs["image_offset"]
        self.face_detection = cv2.CascadeClassifier(kwargs["detection_model_path"])
        self.emotion_classifier = load_model(kwargs["emotion_model_path"], compile=False)
        self.emotion_target_size = self.emotion_classifier.input_shape[1:3]

    def on_emotion_detected(self, callback):
        self.subscribers.append(callback)

    def emotion_detected(self, emotion):
        for callback in self.subscribers:
            callback(emotion)

    def start(self):
        video_capture = cv2.VideoCapture(0)

        while True:
            bgr_image = video_capture.read()[1]
            gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
            faces = self.face_detection.detectMultiScale(gray_image, 1.3, 5)

            for face_coordinates in faces:
                x1, x2, y1, y2 = apply_offsets(
                    face_coordinates, self.emotion_offsets)
                gray_face = gray_image[y1:y2, x1:x2]

                try:
                    gray_face = cv2.resize(gray_face, (self.emotion_target_size))
                except:
                    continue

                gray_face = preprocess_input(gray_face, True)
                gray_face = np.expand_dims(gray_face, 0)
                gray_face = np.expand_dims(gray_face, -1)

                emotion_prediction = self.emotion_classifier.predict(gray_face)

                emotion_label_arg = np.argmax(emotion_prediction)
                emotion = emotions[emotion_label_arg]

                self.emotion_detected(emotion)

            if cv2.waitKey(1) == 27:
                break  # esc to break
