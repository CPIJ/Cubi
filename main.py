import cv2
import numpy as np
import socket
from emotion_detector import EmotionDetector
from statistics import mode, StatisticsError

emotion_cache = []
min_cache_size = 7
previous_emotion = ''

PORT = 8000
HOST = '192.168.250.2'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def set_led_color(color):
    print(f'Set LED to {color}')


def handle_emotion(emotion):
    global previous_emotion
    emotion_cache.append(emotion)

    if len(emotion_cache) < min_cache_size:
        # Wait until enough emotions are stored.
        return

    try:
        most_common_emotion = mode(emotion_cache)
    except StatisticsError:
        # If there are two or more emotions that are equally present
        # add another emotion to the cache to try get a majority.
        return

    emotion_cache.clear()

    if previous_emotion is most_common_emotion.name:
        # Emotion did not change, don't change the LED.
        return

    client.send(str(most_common_emotion.color).encode())
    previous_emotion = most_common_emotion.name


def main():
    detector = EmotionDetector(
        detection_model_path="resources/face-detector.xml",
        emotion_model_path="resources/emotion-classifier.hdf5",
        image_offset=(20, 40)
    )

    detector.on_emotion_detected(handle_emotion)
    detector.start()


if __name__ == '__main__':
    main()
