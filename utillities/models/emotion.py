import utillities.colors as colors

class Emotion():
    def __init__(self, name, color):
        self.name = name
        self.color = color

basic_emotions = {
    0: Emotion('angry', colors.get('red')),
    1: Emotion('disgust', colors.get('purple')),
    2: Emotion('fear', colors.get('green')),
    3: Emotion('happy', colors.get('yellow')),
    4: Emotion('sad', colors.get('blue')),
    5: Emotion('surprise', colors.get('lightblue')),
    6: Emotion('neutral', colors.get('white')),
}
