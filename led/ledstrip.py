import rpi_ws281x as ws
import colors

from time import sleep

LED_COUNT      = 26   # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0 

def Color(red, green, blue):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (red << 16) | (green << 8) | blue 

class LedStrip:
   
    def __init__(self):
        self.controller = ws.PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
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
	       
        c = Color(color[0], color[1], color[2])
        
        print('original: ' + str(color) + ', converted: ' + str(c))
        
        for i in range(self.controller.numPixels()):
            self.controller.setPixelColor(i, c)
            self.controller.show()
		

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--color')

    args = parser.parse_args()

    strip = LedStrip()
    
    strip.start()
    
    c = colors.get(args.color)
    
    strip.transition_to(c, 100)
    
    sleep(5)
    
    strip.stop()
    
