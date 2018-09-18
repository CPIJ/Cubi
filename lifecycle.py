from aiy.vision.leds import Leds
import time
from music import poweroff_theme, poweron_theme
import colors

leds = Leds()

def startup():
	leds.update(Leds.rgb_on(colors.get('blue')))
	time.sleep(0.2)
	leds.update(Leds.rgb_on(colors.get('yellow')))
	time.sleep(0.2)
	leds.update(Leds.rgb_on(colors.get('purple')))
	leds.update(Leds.rgb_on(colors.get('cyan')))
	leds.update(Leds.rgb_on(colors.get('white')))
	leds.update(Leds.rgb_on(colors.get('green')))
	
	player = aiy.toneplayer.TonePlayer(22)
	player.play(*poweron_theme)

	leds.update(Leds.rgb_off())
	leds.update(Leds.privacy_on())


def power_off():
    leds.update(Leds.rgb_on(colors.get('red')))
    player = aiy.toneplayer.TonePlayer(22)
    player.play(*poweroff_theme)
    time.sleep(1)
    leds.update(Leds.privacy_off())
    leds.update(Leds.rgb_off())