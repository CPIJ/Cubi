import rpi_ws281x as ws
import utillities.colors as colors
import config.ledstrip_config as lc
from time import sleep


class LedStrip:

    def __init__(self):
        self.controller = ws.PixelStrip(
            lc.LED_COUNT, lc.LED_PIN, lc.LED_FREQ_HZ, lc.LED_DMA, lc.LED_INVERT, lc.LED_BRIGHTNESS, lc.LED_CHANNEL)
        self.is_on = False
        self.current_color = (0, 0, 0)

    def start(self):
        assert not self.is_on

        self.controller.begin()
        self.is_on = True

    def stop(self):
        assert self.is_on

        self.transition_to((0, 0, 0), 0)
        self.is_on = False

    def transition_to(self, color, ms):
        r, g, b = self.current_color
        count = 0

        while r != color[0] or g != color[1] or b != color[2]:
            if r < color[0]:
                r += 1
            elif r > color[0]:
                r -= 1

            if g < color[1]:
                g += 1
            elif b > color[1]:
                g -= 1

            if b < color[2]:
                b += 1
            elif b > color[2]:
                b -= 1

            count += 1

            if count % 16 == 0:
                c = colors.convert((r, g, b))

                for i in range(self.controller.numPixels()):
                    self.controller.setPixelColor(i, c)
                    self.controller.show()

        self.current_color = color


if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--color')

    # args = parser.parse_args()

    strip = LedStrip()

    strip.start()

    # c = colors.get(args.color)

    strip.transition_to((255, 255, 255), 100)

    print('sleep 2 sec')
    sleep(2)

    strip.transition_to((255, 0, 0), 100)

    print('sleep 5 sec')
    sleep(2)

    print('stop')
    strip.stop()
