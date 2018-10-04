import utillities.lifecycle as lifecycle
from signal import pause
from aiy.pins import BUTTON_GPIO_PIN
from gpiozero import Button
from utillities.logger import Logger

button = Button(BUTTON_GPIO_PIN, hold_time=2)
system_state = ''
button_pressed_count = 0
system_online = False
log = Logger(__name__)


def on_button_held():
	global system_online
	global button_pressed_count
	
	system_online = not system_online
		
	if not system_online:
		lifecycle.power_off()
		button_pressed_count = 0
	else:
		lifecycle.startup()


def on_button_released():
	global button_pressed_count
	global system_state
	
	if not system_online:
		return
	
	button_pressed_count += 1
	
	if button_pressed_count == 2:
		log.info("Switch to conversation mode.")
		lifecycle.ConversationMode()


	if button_pressed_count == 3:		
		log.info("Switch to training mode.")
		lifecycle.LearningMode()
		button_pressed_count = 1

            							

if __name__ == '__main__':
	button.when_released = on_button_released
	button.when_held = on_button_held
	log.info('Buttons ready.')
	
	pause()
