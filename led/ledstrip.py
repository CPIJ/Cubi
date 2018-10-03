import rpi_ws281x as ws
import utillities.colors as colors
import config.ledstrip_config as lc
from time import sleep


class LedStrip:

    def __init__(self):
        self.controller = ws.PixelStrip(lc.LED_COUNT, lc.LED_PIN, lc.LED_FREQ_HZ, lc.LED_DMA, lc.LED_INVERT, lc.LED_BRIGHTNESS, lc.LED_CHANNEL)
        self.is_on = False
        self.current_color = (0, 0, 0)

    def start(self):
        assert not self.is_on

        self.controller.begin()
        self.is_on = True

    def stop(self):
        assert self.is_on

        self.transition_to(colors.get('black'), 0)
        self.is_on = False

    def transition_to(self, color, ms):
        for i in range(self.controller.numPixels()):
            curr_col = self.controller.getPixelColor(i)

            b = curr_col & 0xFF
            g = (curr_col >> 8) & 0xFF
            r = (curr_col >> 16)

            while r != color[0] or g != color[1] or b != color[2]:
                r = r + 1 if r < color[0] else r - 1
                g = g + 1 if g < color[1] else g - 1
                b = b + 1 if b < color[2] else b - 1

                print((r,g,b))

                c = colors.convert((r, g, b))

                self.controller.setPixelColor(i, c)
                self.controller.show()
                sleep(0.1)


if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--color')

    # args = parser.parse_args()

    strip = LedStrip()

    strip.start()

    # c = colors.get(args.color)

    strip.transition_to((255, 255, 255), 100)

    sleep(5)

    strip.transition_to((255, 0, 0), 100)

    strip.stop()
