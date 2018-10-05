import utillities.lifecycle as lifecycle
from signal import pause
from aiy.pins import BUTTON_GPIO_PIN
from gpiozero import Button
from utillities.logger import Logger
from config.socket_config import get_server_config
from utillities.socket_protocol import Command
from utillities.classes.socket_server import SocketServer
from utillities.classes.socket_client import SocketClient

button = Button(BUTTON_GPIO_PIN, hold_time=2)
system_state = ''
button_pressed_count = 0
system_online = False
log = Logger(__name__)
logic_client = None

def on_message(message, sender):
	global button_pressed_count
	global logic_client
	global system_online
	
	command_succesful = True
	command = Command.parse(message)
	
	if command.action == "SET_MODE":	
		if command.parameter == "CONVERSATION" and system_online:				
			log.info("Switch to conversation mode.")
			lifecycle.ConversationMode()
			button_pressed_count = 2
			
		elif command.parameter == "TRAINING" and system_online:	
			log.info("Switch to training mode.")
			lifecycle.LearningMode()
			button_pressed_count = 1
			
		elif command.parameter == "STANDBY":
			on_button_held()
			
		else:
			command_succesful = False
			log.error('Invalid parameter: ' + command.parameter)
		
		if command_succesful:
			log.debug('aaaaa')
			logic_client.send(command.serialize())
		else:
			print('Failed to send ' + command.serialize() + ', Cubi in standby: ' + str(not system_online))
			
	else:
		log.error('Unkown command')


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
		

def init_server():
	server_config = get_server_config('IO_SERVER')
	server = SocketServer(server_config.port, 'IO_SERVER')
	server.message_received(on_message)
	server.start()

			
def init_button():
	button.when_released = on_button_released
	button.when_held = on_button_held
	log.info('Buttons ready.')


def init_logic_client():
	global logic_client
	
	server_config = get_server_config('LOGIC_SERVER')
	logic_client = SocketClient(server_config.host, server_config.port)
	

def main():
	init_button()
	init_server()
	init_logic_client()
		
	pause()

if __name__ == '__main__':
	main()
