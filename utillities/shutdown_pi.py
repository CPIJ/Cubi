#!/bin/python

import RPi.GPIO as GPIO 
import time 
import os

from aiy.pins import BUTTON_GPIO_PIN
from gpiozero import Button
from gpiozero import LED
from aiy.pins import LED_1

button = Button(BUTTON_GPIO_PIN)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#def Restart(channel):
	#os.system("sudo shutdown -h now")
	
#GPIO.add_event_detect(23, GPIO.FALLING, callback = Restart, bouncetime = 2000)


def on_button_pressed():
    os.system("sudo shutdown -r now")


def main():
    while 1:
        time.sleep(1)


if __name__ == '__main__':
    button.when_pressed = on_button_pressed
    main()
