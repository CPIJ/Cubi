import lifecycle
import random
import os
import socket
import time
#from ledstrip import *
from emotion_detector import EmotionDetector
from statistics import mode
from signal import pause
from statistics import mode, StatisticsError
from aiy.pins import BUTTON_GPIO_PIN
from threading import Thread
from threading import Timer
from gpiozero import Button
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from aiy.pins import PIN_A

emotion_cache = []
min_cache_size = 3
previous_emotion = ''
button = Button(BUTTON_GPIO_PIN, hold_time=5)
system_state = 'test'
button_pressed_count = 0
detector = None
random_chosen_color = None
timer_value = 10
timer_ended = False
correct_gues = False
Learningmode_started = False
Colors = ['red','green','yellow','blue','purple','cyan','white','lightblue']
timer = None
learning_mode_thread = None


def set_led_color(emotion_color):
	global Learningmode_started
	global system_state
	global correct_gues
	global timer_ended
	
	
	if system_state == "ConversationMode":
		#kleur laten zien op ledstrip
		lifecycle.ledstrip.transition_to_Color(emotion_color, 100)

	
	if system_state == "LearningMode":
		if random_chosen_color == emotion_color:
			correct_gues = True
			Learningmode_started = False
						
			#goed dus groen laten zien
			lifecycle.ledstrip.transition_to_string("green")
			
		else:
			#print("test")
			if timer_ended == False:
				lifecycle.ledstrip.transition_to_string("red")
				time.sleep(1)
				lifecycle.ledstrip.transition_to_string("white")
				time.sleep(1)
				lifecycle.ledstrip.transition_to_string("black")
				time.sleep(1)
			#fout dus zoeken laten zien?

def handle_emotion(emotion):
	global previous_emotion
	emotion_cache.append(emotion)

	if len(emotion_cache) < min_cache_size:
		# Wait until enough emotions are stored.
		return

	try:
		most_common_emotion = mode(emotion_cache)
	except StatisticsError:
		# If there are two or more emotions that are equally present
		# add another emotion to the cache to try get a majority.
		return

	emotion_cache.clear()

	if previous_emotion is most_common_emotion.name:
		# Emotion did not change, don't change the LED.
		return
	print(most_common_emotion.name)
	set_led_color(most_common_emotion.color)
	#previous_emotion.name = most_common_emotion.name
	previous_emotion = most_common_emotion.name

def timeout():
	global Learningmode_started
	global timer_ended
	
	detector.stop()
	timer_ended = True
	print("timer klaar")
	
	lifecycle.ledstrip.transition_to_string("red")
	time.sleep(3)
	
	Learningmode_started = False
	learning_mode_thread = Thread(target=start_learning_mode(system_state))
	learning_mode_thread.start()
	
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
	
	
def start_learning_mode(system_state):
	global random_chosen_color
	global timer
	global Learningmode_started
	if Learningmode_started == False:
		detector.stop()
		Learningmode_started = True
		random_chosen_color = None
		correct_gues = False
		timer_ended = False;
		
		#vraag een random kleur op 
		random_chosen_color = random.choice(Colors)
		print("random kleur is: ", random_chosen_color)
		
		#start training mode op ledstrip
		lifecycle.ledstrip.transition_to_string(random_chosen_color)
		 
		#start timer 
		timer = Timer(20, timeout)
		timer.start()
		print("---timer started---")
		
		#detecteer kleur 
		detector.Continue()
		
		#laat zien of goeie kleur

def on_button_released():
	global button_pressed_count
	global correct_gues
	global timer_ended
	global Learningmode_started
	global timer
	global learning_mode_thread
	global system_state
	
	button_pressed_count += 1
	if button_pressed_count == 1:
		system_state = "ConversationMode"
		print("---------Conversation mode started--------")
		lifecycle.ConversationMode()
		if detector.stopped == True:
			detector.Continue()

	if button_pressed_count == 2:		
		system_state = "LearningMode"
		print("---------Learning mode started--------")
		lifecycle.LearningMode()

		if system_state == "LearningMode":  
			if Learningmode_started == False:
				learning_mode_thread = Thread(target=start_learning_mode(system_state))
				learning_mode_thread.start()
				
	if button_pressed_count == 3:
		timer.cancel()
		Learningmode_started = False
		button_pressed_count = 0
		on_button_released()

def start_emotion_detection():
    detector.on_emotion_detected(handle_emotion)
    detector_thread = Thread(target=detector.start)
    detector_thread.start()
            
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
	
	detector = EmotionDetector(
        detection_model_path="resources/face-detector.xml",
        emotion_model_path="resources/emotion-classifier.hdf5",
        image_offset=(20, 40))
        
	detector.on_emotion_detected(handle_emotion)
	UI_thread = Thread(target=UI)
	UI_thread.start()
	#UI_thread.join()
	
	lifecycle.startup()
	detector.stop()
	detector.run()
	#detector.stop()
	#button.when_pressed = on_button_pressed
	#button.when_released = on_button_released
	#button.when_held = lifecycle.power_off
	
	#UI_thread.join()
	pause()
