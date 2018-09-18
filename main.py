import cv2
import numpy as np
import lifecycle
from emotion_detector import EmotionDetector
from statistics import mode, StatisticsError
from gpiozero import Button
from aiy.vision.pins import BUTTON_GPIO_PIN
from signal import pause

emotion_cache = []
min_cache_size = 7
previous_emotion = ''
button = Button(BUTTON_GPIO_PIN)
system_state = ''
button_pressed_count = 0


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

    set_led_color(most_common_emotion.color)
    previous_emotion = most_common_emotion.name


def on_button_pressed():
    global button_pressed_count

    if button.is_pressed:
        button_pressed_count += 1

        if button_pressed_count == 1:
            system_state = "PowerOn"
            lifecycle.startup()
            start_emotion_detection()

        if button_pressed_count == 2:
            system_state = "DemoMode"

        if button_pressed_count == 3:
            lifecycle.power_off()
            system_state = "Offline"
            button_pressed_count = 0


def start_emotion_detection():
    detector = EmotionDetector(
        detection_model_path="resources/face-detector.xml",
        emotion_model_path="resources/emotion-classifier.hdf5",
        image_offset=(20, 40)
    )

    detector.on_emotion_detected(handle_emotion)
    detector.start()


def main():
    while pause():
        if system_state == "PowerOn":
            pass

        if system_state == "DemoMode":
            pass


if __name__ == '__main__':
    button.when_pressed = on_button_pressed
    main()
