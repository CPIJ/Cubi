def Color(red, green, blue):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (red << 16) | (green << 8) | blue 


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

def convert(color):
    return Color(color[0], color[1], color[2])

def convert_to_rgb(number):
    b = number & 0xFF
    g = (number >> 8) & 0xFF 
    r = (number >> 16) & 0xFF

    return (r, g, b)