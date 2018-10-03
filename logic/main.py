from utillities.classes.socketclient import SocketClient
from utillities.classes.socketserver import SocketServer
from ai.emotion_detector import EmotionDetector
from config.socket_config import LED_SERVER, LOGIC_SERVER
import utillities.socket_protocol as socket_protocol

detector = None
ledstrip_client = None
socket_server = None


def handle_emotion(emotion, kwargs):
    client = kwargs['client']
    client.send(f'Color:{str(emotion.color)}')


def handle_socket_message(message):
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

    socket_server = SocketServer(LOGIC_SERVER.port)
    socket_server.message_recevied(handle_socket_message)
    socket_server.start()


def init_detector():
    global detector

    detector = EmotionDetector(
        detection_model_path="logic/ai/resources/face-detector.xml",
        emotion_model_path="logic/ai/resources/emotion-classifier.hdf5",
        image_offset=(20, 40)
    )

    detector.on_emotion_detected(handle_emotion)


def main():
    global ledstrip_client
    
    ledstrip_client = SocketClient(LED_SERVER.host, LED_SERVER.port)
    start_server()
    init_detector()


if __name__ == "__main__":
    main()
