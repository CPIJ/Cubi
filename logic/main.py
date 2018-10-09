import argparse
import random
import utillities.colors as colors

from threading import Timer
from time import sleep
from utillities.logger import Logger
from utillities.socket_protocol import Command, CommandType
from utillities.classes.socket_client import SocketClient
from utillities.classes.socket_server import SocketServer
from utillities.models.emotion import get_level, toggle_emotion
from ai.emotion_detector import EmotionDetector
from config.socket_config import get_server_config

detector = None
ledstrip_client = None
io_client = None
socket_server = None
is_test = False
state = ''
training_emotion = None
training_timer = None
log = Logger(__name__)
is_standby = True
level = 1

def start_io_client():
    global io_client

    server_config = get_server_config('IO_SERVER', is_test)
    log.debug('Connecting to IO_SERVER at ' + str(server_config))
    io_client = SocketClient(server_config.host, server_config.port)
    log.debug('IO_SERVER Connected')

def close():
    set_to_black_cmd = Command.create(CommandType.set_color, '(0, 0, 0)').serialize()
    exit_cmd = Command.create(CommandType.exit).serialize()

    ledstrip_client.send(set_to_black_cmd)
    ledstrip_client.send(exit_cmd)

    io_client.send(set_to_black_cmd)
    io_client.send(exit_cmd)


def handle_training_result(color):
    training_timer.cancel()
    detector.stop()

    command = Command.create(CommandType.set_color, str(color)).serialize()
    ledstrip_client.send(command)
    io_client.send(command)

    sleep(3)

    training_cycle()


def handle_emotion(emotion):
    global training_timer
    global training_emotion
    global ledstrip_client
    global state

    if state == "TRAINING":
        if emotion == training_emotion:
            log.debug('Guessed correctly')
            io_client.send('PLAY_SOUND:RIGHT')
            handle_training_result(emotion.color)

        else:
            log.debug('Guessed not correctly, canceled timer.')
            io_client.send('PLAY_SOUND:WRONG')
            handle_training_result(emotion.color)

    elif state == "CONVERSATION":
        if not emotion.enabled:
            return

        command = Command.create(CommandType.set_color, str(emotion.color)).serialize()
        ledstrip_client.send(command)
        io_client.send(command)

    elif state == "STANDBY":
        if training_timer is not None:
            training_timer.cancel()

    else:
        log.error('Unkown state, cannot handle emotion')


def timeout():
    detector.stop()
    command = Command.create(CommandType.set_color,str((255, 0, 0))).serialize()
    ledstrip_client.send(command)
    io_client.send(command)

    sleep(3)
    training_cycle()


def blink(color):
    global ledstrip_client
    global state

    for i in range(3):
        if state != "TRAINING":
            break

        log.info('Blink ' + str(3 - i))

        command = Command.create(CommandType.set_color, str(color))
        ledstrip_client.send(command.serialize())
        io_client.send(command.serialize())

        sleep(1)

        command = Command.create(CommandType.set_color, str(colors.get('white')))
        ledstrip_client.send(command.serialize())
        io_client.send(command.serialize())

        sleep(1)

def get_random_emotion(whitelist = ['happy', 'angry', 'surprise']):
    emotions = [dictionary[1] for dictionary in get_level(1).items()]
    filtered = filter(lambda emotion: emotion.name in whitelist, emotions)

    return random.choice(list(filtered))
    

def training_cycle():
    log.debug('Entering training cycle.')
    global training_timer
    global training_emotion

    detector.stop()
    log.debug('Stopped detector.')

    training_emotion = get_random_emotion()
    log.debug('Random choice: ' + str(training_emotion.name))

    command = Command.create(CommandType.set_color, str(training_emotion.color))
    ledstrip_client.send(command.serialize())
    io_client.send(command.serialize())

    training_timer = Timer(20, timeout)

    blink(training_emotion.color)

    log.debug('Starting detector.')
    detector.start()


def handle_socket_message(message, sender):
    global state
    global is_standby
    global ledstrip_client
    global level

    command = Command.parse(message)

    log.info(command.serialize())

    if command.action == "EXIT":
        close()
    elif command.action == "READY":
        if command.parameter == "IO_SERVER":
            start_io_client()
    elif command.action == "SET_LEVEL":
        log.debug('Change level: ' + command.parameter)
        detector.level = int(command.parameter)

    elif command.action == "TOGGLE_EMOTION":
        log.debug('Toggle emotion: ' + command.parameter)
        toggle_emotion(command.parameter.lower())

    elif command.action == "SET_MODE":
        state = command.parameter

        log.debug('Got mode change: ' + state)

        if state == "CONVERSATION":
            detector.start()

        elif state == "TRAINING":
            detector.emotion_cache.clear()
            training_cycle()

        elif state == "STANDBY":
            is_standby = not is_standby

            c = (0,0,0)

            if is_standby:
                detector.stop()
                level = 1
            else:
                c = (255,255,255)
                detector.start()
            
            command = Command.create(CommandType.set_color, str(c))
            ledstrip_client.send(command.serialize())

        else:
            log.error('Unkown state: ' + state)

    else:
        print('Unkown command')


def start_server():
    global socket_server

    server_config = get_server_config('LOGIC_SERVER', is_test)

    log.debug('Starting LOGIC_SERVER at ' + str(server_config))

    socket_server = SocketServer(server_config.port, "LOGIC_SERVER")
    socket_server.message_received(handle_socket_message)
    socket_server.start()

    log.debug('LOGIC_SERVER Started')


def start_ledstrip_client():
    global ledstrip_client

    server_config = get_server_config('LED_SERVER', is_test)
    log.debug('Connecting to LED_SERVER at ' + str(server_config))
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
    start_server()
    init_detector()


if __name__ == "__main__":
    is_test = False

    main()
