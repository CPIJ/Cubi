import argparse
import random
import utillities.colors as colors

from threading import Timer
from time import sleep
from utillities.logger import Logger
from utillities.socket_protocol import Command, CommandType
from utillities.classes.socket_client import SocketClient
from utillities.classes.socket_server import SocketServer
from utillities.models.emotion import basic_emotions as emotions
from ai.emotion_detector import EmotionDetector
from config.socket_config import get_server_config

detector = None
ledstrip_client = None
socket_server = None
is_test = False
state = ''
training_emotion = None
training_timer = None
log = Logger(__name__)
is_guessing = False

def close():
    set_to_black_cmd = Command.create(
        CommandType.set_color, '(0, 0, 0)').serialize()
    exit_cmd = Command.create(CommandType.exit).serialize()

    ledstrip_client.send(set_to_black_cmd)
    ledstrip_client.send(exit_cmd)


def handle_emotion(emotion):
    global training_timer
    global training_emotion
    global ledstrip_client
    global state
    global is_guessing

    if state == "TRAINING":        
        if emotion == training_emotion:
            log.debug('Guessed correctly')
            command = Command.create(CommandType.set_color, colors.get('green')).serialize()
            ledstrip_client.send(command)

        else:
            training_timer.cancel()
            log.debug('Guessed not correctly, canceled timer.')
            command = Command.create(CommandType.set_color, colors.get('red')).serialize()
            ledstrip_client.send(command)
            training_cycle()

    elif state == "CONVERSATION":
        command = Command.create(
            CommandType.set_color, str(emotion.color)).serialize()
        ledstrip_client.send(command)

    else:
        log.error('Unkown state, cannot handle emotion')


def timeout():
    detector.stop()
    command = Command.create(CommandType.set_color,str((255, 0, 0))).serialize()
    ledstrip_client.send(command)
    sleep(3)
    training_cycle()


def knipper(color):
    global ledstrip_client

    for i in range(5):
        ledstrip_client.send(Command.create(CommandType.set_color, str(color)).serialize())
        sleep(1)
        ledstrip_client.send(Command.create(CommandType.set_color, str((0,0,0))).serialize())

def training_cycle():
    log.debug('Entering training cycle.')
    global training_timer
    global training_emotion
    global is_guessing

    detector.stop()
    log.debug('Stopped detector.')

    training_emotion = random.choice(emotions)
    log.debug('Random choice: ' + str(training_emotion))

    ledstrip_client.send(Command.create(CommandType.set_color, str(training_emotion.color)).serialize())
    training_timer = Timer(20, timeout)

    knipper(training_emotion)

    log.debug('Starting detector.')
    detector.start()


def handle_socket_message(message, sender):
    global state

    command = Command.parse(message)

    if command.action == "EXIT":
        close()

    elif command.action == "SET_MODE":
        state = command.parameter

        log.debug('Got mode change: ' + state)

        if state == "CONVERSATION":
            detector.start()

        elif state == "TRAINING":
            training_cycle()

        else:
            log.error('Unkown state: ' + state)

    else:
        print('Unkown command')


def start_server():
    global socket_server

    server_config = get_server_config('LOGIC_SERVER', is_test)

    log.debug('Starting LOGIC_SERVER at' + str(server_config))

    socket_server = SocketServer(server_config.port, "LOGIC_SERVER")
    socket_server.message_received(handle_socket_message)
    socket_server.start()

    log.debug('LOGIC_SERVER Started')


def start_ledstrip_client():
    global ledstrip_client

    server_config = get_server_config('LED_SERVER', is_test)
    log.debug('Connecting to LED_SERVER at' + str(server_config))
    ledstrip_client = SocketClient(server_config.host, server_config.port)
    log.debug('LED_SERVER Connected')


def init_detector():
    global detector

    detector = EmotionDetector(
        detection_model_path="logic/ai/resources/face-detector.xml",
        emotion_model_path="logic/ai/resources/emotion-classifier.hdf5",
        image_offset=(20, 40)
    )

    detector.on_emotion_detected(handle_emotion)

    detector.init()


def main():
    start_ledstrip_client()

    ledstrip_client.send(Command.create(
        CommandType.set_color, '(0,0,0)').serialize())

    start_server()
    init_detector()


if __name__ == "__main__":
    is_test = False

    main()
