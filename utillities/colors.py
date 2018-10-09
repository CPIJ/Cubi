import json

colors = []

def load_colors():
    global colors

    if len(colors) == 0:
        with open('config/colors.json') as file:
            data = json.load(file)
            colors = data
    
    return colors


def Color(red, green, blue):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (red << 16) | (green << 8) | blue


def get(name):
    colors = load_colors()
    switch = {}

    for color in colors:
        switch[color["name"]] = eval(color["value"])

    return switch.get(name, (255, 255, 255))


def convert(color):
    return Color(color[0], color[1], color[2])


def convert_to_rgb(number):
    b = number & 0xFF
    g = (number >> 8) & 0xFF
    r = (number >> 16) & 0xFF

    return (r, g, b)