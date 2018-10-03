import numpy as np


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
