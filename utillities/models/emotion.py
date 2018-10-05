import utillities.colors as colors
from collections import namedtuple

Emotion = namedtuple('Emotion', ['name', 'color', 'enabled'])
black_list = []
levels = [1, 2, 3]

def toggle_emotion(name):
    if name in black_list:
        black_list.remove(name)
    else:
        black_list.append(name)

    print('DEBUG: black_list state: ' + str(black_list))

def get_emotion_color(name, level):
    switch = {
        'angry': {
            1: colors.get('red'),
            2: colors.get('red'),
            3: colors.get('white')
        },
        'disgust': {
            1: colors.get('purple'),
            2: colors.get('red'),
            3: colors.get('white')
        },
        'fear': {
            1: colors.get('green'),
            2: colors.get('red'),
            3: colors.get('white')
        },
        'happy': {
            1: colors.get('yellow'),
            2: colors.get('green'),
            3: colors.get('white')
        },
        'sad': {
            1: colors.get('blue'),
            2: colors.get('red'),
            3: colors.get('white')
        },
        'surprise': {
            1: colors.get('lightblue'),
            2: colors.get('green'),
            3: colors.get('white')
        },
        'neutral': {
            1: colors.get('white'),
            2: (0, 0, 0),
            3: (0, 0, 0)
        },
    }

    emotion_levels = switch.get(name)

    if emotion_levels is None:
        raise ValueError()

    level_colors = emotion_levels.get(level)

    if level_colors is None:
        raise ValueError()

    return level_colors


def get_emotion(name, level):
    return Emotion(name, get_emotion_color(name, level), name not in black_list)


def get_level(n):
    switch = {}

    for level in levels:
        switch[level] = {
            0: get_emotion('angry', level),
            1: get_emotion('disgust', level),
            2: get_emotion('fear', level),
            3: get_emotion('happy', level),
            4: get_emotion('sad', level),
            5: get_emotion('surprise', level),
            6: get_emotion('neutral', level),
        }

    level = switch.get(n)

    if level is None:
        raise ValueError('Unkown level: ' + n)

    return level
