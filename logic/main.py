import utillities.socket_protocol as socket_protocol
import argparse

from utillities.classes.socket_client import SocketClient
from utillities.classes.socket_server import SocketServer
from ai.emotion_detector import EmotionDetector
from config.socket_config import get_server_config
from utillities.socket_protocol import CommandType


detector = None
ledstrip_client = None
socket_server = None
is_test = False


def handle_emotion(emotion):
    command = socket_protocol.create_command(CommandType.set_led, str(emotion.color))
    serialized = socket_protocol.serialize_command(command)

    ledstrip_client.send(serialized)


def handle_socket_message(message, sender):
    global detector

    command = socket_protocol.parse_command(message)

    switch = {
        "SET_MODE:CONVERSATION": lambda: detector.start(),
        "SET_MODE:TRAINING": lambda: detector.stop(),
        "EXIT": lambda: print('Zet em uit'),
    }

    func = switch.get(message, lambda: print('Unknown command'))

    func()


def start_server():
    global socket_server

    server_config = get_server_config('LOGIC_SERVER', is_test)

    socket_server = SocketServer(server_config.port, "LOGIC_SERVER")
    socket_server.message_received(handle_socket_message)
    socket_server.start()


def start_ledstrip_client():
    global ledstrip_client

    server_config = get_server_config('LED_SERVER', is_test)
    ledstrip_client = SocketClient(server_config.host, server_config.port)


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

    detector.start()


if __name__ == "__main__":
    is_test = False

    main()
