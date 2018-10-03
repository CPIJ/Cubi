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


def close():
    set_to_black_cmd = Command.create(CommandType.set_color, '(0, 0, 0)').serialize()
    exit_cmd = Command.create(CommandType.exit).serialize()

    ledstrip_client.send(set_to_black_cmd)
    ledstrip_client.send(exit_cmd)


def handle_emotion(emotion):
    global training_timer
    global training_emotion

    if state == "TRAINING":
        if emotion == training_emotion:
            command = Command.create(CommandType.set_color, colors.get('green')).serialize()
        else:
            training_timer.cancel()
            command = Command.create(CommandType.set_color, colors.get('red')).serialize()

    elif state == "CONVERSATION":
        command = Command.create(CommandType.set_color, str(emotion.color)).serialize()
        ledstrip_client.send(command)
    


def training_cycle():
    global training_timer
    global training_emotion

    detector.stop()

    training_emotion = random.choice(emotions)

    ledstrip_client.send(Command.create(CommandType.set_color, str(training_emotion.color)).serialize())
    training_timer = Timer(20, timeout)

    detector.start()



def timeout():
    detector.stop()

    command = Command.create(CommandType.set_color,str((255, 0, 0))).serialize()

    ledstrip_client.send(command)

    sleep(3)

    training_cycle()


def handle_socket_message(message, sender):
    command = Command.parse(message)

    if command.action == "EXIT":
        close()

    elif command.action == "SET_MODE":
        state = command.parameter

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


def main():
    start_ledstrip_client()
    start_server()
    init_detector()
    detector.init()


if __name__ == "__main__":
    is_test = False

    main()
