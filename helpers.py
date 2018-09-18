import numpy as np
import colors

class Emotion():
    def __init__(self, name, color):
        self.name = name
        self.color = color


emotions = {
    0: Emotion('angry', colors.get('red')),
    1: Emotion('disgust', colors.get('purple')),
    2: Emotion('fear', colors.get('green')),
    3: Emotion('happy', colors.get('yellow')),
    4: Emotion('sad', colors.get('blue')),
    5: Emotion('surprise', colors.get('lightblue')),
    6: Emotion('neutral', colors.get('white')),
}


def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x


def apply_offsets(face_coordinates, offsets):
    x, y, width, height = face_coordinates
    x_off, y_off = offsets
    return (x - x_off, x + width + x_off, y - y_off, y + height + y_off)


def get_color(emotion, probability):
    color = None

    if emotion == 'angry':
        color = probability * np.asarray((255, 0, 0))
    elif emotion == 'sad':
        color = probability * np.asarray((0, 0, 255))
    elif emotion == 'happy':
        color = probability * np.asarray((255, 255, 0))
    elif emotion == 'surprise':
        color = probability * np.asarray((0, 255, 255))
    else:
        color = probability * np.asarray((0, 255, 0))

    return color.astype(int).tolist()
