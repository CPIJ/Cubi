import cv2
import numpy as np
from keras.models import load_model
from ai.helpers import *
from statistics import mode, StatisticsError
from threading import Thread
from utillities.models.emotion import get_level
from utillities.logger import Logger

log = Logger(__name__)

class EmotionDetector():
    def __init__(self, **kwargs):
        self.subscribers = []
        self.emotion_offsets = kwargs["image_offset"]
        self.face_detection = cv2.CascadeClassifier(
            kwargs["detection_model_path"])
        self.emotion_classifier = load_model(
            kwargs["emotion_model_path"], compile=False)
        self.emotion_target_size = self.emotion_classifier.input_shape[1:3]
        self.emotion_cache = []
        self.min_cache_size = 14
        self.previous_emotion = ''
        self.is_running = False
        self.level = 1

    def on_emotion_detected(self, callback):
        self.subscribers.append(callback)

    def emotion_detected(self, emotion):
        self.emotion_cache.append(emotion)

        if len(self.emotion_cache) < self.min_cache_size:
            # Wait until enough emotions are stored.
            return

        try:
            most_common_emotion = mode(self.emotion_cache)
        except StatisticsError:
            # If there are two or more emotions that are equally present
            # add another emotion to the cache to try get a majority.
            return

        self.emotion_cache.clear()

        if self.previous_emotion is most_common_emotion.name:
            # Emotion did not change, don't change the LED.
            return

        self.previous_emotion = most_common_emotion.name

        for callback in self.subscribers:
            callback(most_common_emotion)

    def stop(self):
        log.debug('Stopping emotion detector.')
        self.emotion_cache.clear()
        self.is_running = False

    def start(self):
        log.debug('Starting emotion detector.')
        self.emotion_cache.clear()
        self.is_running = True

    def init(self):
        video_capture = cv2.VideoCapture(0)
        has_frame, bgr_image = video_capture.read()

        while True:
            if not self.is_running:
                continue
            
            has_frame, bgr_image = video_capture.read()

            if not has_frame:
                continue

            gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
            face = next(iter(self.face_detection.detectMultiScale(gray_image, 1.3, 5)), None)

            if face is None:
                continue

            x1, x2, y1, y2 = apply_offsets(face, self.emotion_offsets)
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
            emotion = get_level(self.level)[emotion_label_arg]

            self.emotion_detected(emotion)

            if cv2.waitKey(1) == 27:
                break  # esc to break
