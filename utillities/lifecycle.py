import time
import utillities.colors as colors
import os
import aiy.toneplayer
from aiy.leds import Leds
from utillities.music import poweroff_theme, poweron_theme
from utillities.logger import Logger

log = Logger(__name__)
leds = Leds()
color_cycle = ['blue', 'yellow', 'purple', 'cyan', 'white', 'green']
is_pulsing = False

def transition_to(from_color, to_color):
	r, g, b = from_color
	
	while r != to_color[0] or g != to_color[1] or b != to_color[2]:
		if r < to_color[0]:
			r += 1
		elif r > to_color[0]:
			r -= 1

		if g < to_color[1]:
			g += 1
		elif g > to_color[1]:
			g -= 1

		if b < to_color[2]:
			b += 1
		elif b > to_color[2]:
			b -= 1
			
		leds.update(Leds.rgb_on((r, g, b)))
		
		time.sleep(0.0008)


def startup():
	log.info("Entering startup")
		
	for (index, color) in enumerate(color_cycle):
		if index > 0:
			c1 = colors.get(color_cycle[index - 1])
			c2 = colors.get(color_cycle[index])
			transition_to(c1, c2)
		else:	
			leds.update(Leds.rgb_on(colors.get(color)))
			time.sleep(0.2)

	leds.update(Leds.privacy_on())

	
	
def ConversationMode():
	leds.update(Leds.rgb_on(colors.get('blue')))


def LearningMode():
	leds.update(Leds.rgb_on(colors.get('green')))


def stand_by():
	global state
	

def power_off():
	global state
	log.info("Entering standby")
	x = 25
	leds.update(Leds.rgb_on((x,x,x)))
	leds.update(Leds.privacy_off())
	
	

	
	

