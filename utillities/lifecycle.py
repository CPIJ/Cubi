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

def startup():
	log.info("Entering startup")
	
	for color in color_cycle:	
		leds.update(Leds.rgb_on(colors.get(color)))
		time.sleep(0.2)

	leds.update(Leds.privacy_on())

	
	
def ConversationMode():
	leds.update(Leds.rgb_off())


def LearningMode():
	leds.update(Leds.rgb_on(colors.get('green')))


def power_off():
	log.info("---------Powering down--------")
	
	leds.update(Leds.rgb_on(colors.get('red')))
	time.sleep(1)
	leds.update(Leds.privacy_off())
	leds.update(Leds.rgb_off())
	time.sleep(1)

