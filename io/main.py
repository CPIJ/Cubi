import lifecycle
import os
import socket
import time

from statistics import mode
from signal import pause
from statistics import mode, StatisticsError
from aiy.pins import BUTTON_GPIO_PIN
from threading import Thread
from gpiozero import Button
from gpiozero import LED


button = Button(BUTTON_GPIO_PIN, hold_time=5)
system_state = ''
button_pressed_count = 0
	
def on_button_pressed():
	pass
	#timer = None
	#while button.is_pressed:
		#if system_state == "PowerOn" or system_state == "ConversationMode" or system_state == "LearningMode":
			#timer = Timer(5, lifecycle.poweroff)
			#timer.start()
			
			#timer.join()
			#os.system("sudo shutdown -r now")
	#timer.stop
	

def on_button_released():
	global button_pressed_count
	global system_state
	
	button_pressed_count += 1
	if button_pressed_count == 1:
		system_state = "ConversationMode"
		print("---------Conversation mode started--------")
		lifecycle.ConversationMode()
		#stuur naar Logic conversationmode

	if button_pressed_count == 2:		
		system_state = "LearningMode"
		print("---------Learning mode started--------")
		lifecycle.LearningMode()
		#stuur naar Logic learningmode
				
	if button_pressed_count == 3:
		timer.cancel()
		Learningmode_started = False
		button_pressed_count = 0
		on_button_released()
            
def main():
	while pause():
		if system_state == "test":
			pass
			
def UI():
	button.when_pressed = on_button_pressed
	button.when_released = on_button_released
	button.when_held = lifecycle.power_off
				

if __name__ == '__main__':
	system_state = "PowerOn"
	lifecycle.ledstrip.transition_to_string("blue")
	
	UI_thread = Thread(target=UI)
	UI_thread.start()
	
	lifecycle.startup()
	button.when_pressed = on_button_pressed
	button.when_released = on_button_released
	button.when_held = lifecycle.power_off
	
	pause()
