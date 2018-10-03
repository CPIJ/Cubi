import time
import colors
import os
import aiy.toneplayer

from ledstrip import *
from aiy.leds import Leds
from music import poweroff_theme, poweron_theme

leds = Leds()
ledstrip = LedStrip()
ledstrip.start()


def startup():
	print("---------starting up--------")
	ledstrip.transition_to_string("white")
	leds.update(Leds.rgb_on(colors.get('blue')))
	time.sleep(0.5)
	leds.update(Leds.rgb_on(colors.get('yellow')))
	time.sleep(0.5)
	leds.update(Leds.rgb_on(colors.get('purple')))
	time.sleep(0.5)
	leds.update(Leds.rgb_on(colors.get('cyan')))
	time.sleep(0.5)
	leds.update(Leds.rgb_on(colors.get('white')))
	time.sleep(0.5)
	leds.update(Leds.rgb_on(colors.get('green')))

	player = aiy.toneplayer.TonePlayer(22)
	player.play(*poweron_theme)

	leds.update(Leds.privacy_on())

	ledstrip.transition_to_string("blue")
	
	
def ConversationMode():
	leds.update(Leds.rgb_off())
	time.sleep(0.2)

def LearningMode():
	leds.update(Leds.rgb_on(colors.get('green')))
	time.sleep(0.2)

def power_off():
	print("---------Powering down--------")
	leds.update(Leds.rgb_on(colors.get('red')))
	player = aiy.toneplayer.TonePlayer(22)
	player.play(*poweroff_theme)
	time.sleep(1)
	leds.update(Leds.privacy_off())
	leds.update(Leds.rgb_off())
	sleep(1)
	#ledstrip_socket.send("shutdown".encode())
	#os.system("sudo shutdown -h now")
