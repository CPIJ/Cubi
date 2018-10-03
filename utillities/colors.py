def get(name):
    switch = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'yellow': (255, 255, 0),
        'blue': (0, 0, 255),
        'purple': (255, 0, 255),
        'cyan': (0, 255, 255),
        'white': (255, 255, 255),
    }

    return switch.get(name, (0, 0, 0))
