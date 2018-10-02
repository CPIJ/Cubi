from connections import SocketServer, SocketClient
from emotion_detector import EmotionDetector

detector = None
ledstrip_client = None
socket_server = None

def handle_emotion(emotion, kwargs):
    client = kwargs['client']
    client.send(f'Color:{str(emotion.color)}')


def handle_socket_message(message):
    global detector

    switch = {
        "SET_MODE:CONVERSATION": lambda: detector.start(),
        "SET_MODE:TRAINING": lambda: detector.stop(),
        "EXIT": lambda: print('Zet em uit'),
    }

    func = switch.get(message, lambda: print('Unknown command'))

    func()

def main():
    global ledstrip_client
    global socket_server
    global detector

    ledstrip_client = SocketClient('192.168.250.1', 8000)

    socket_server = SocketServer(9000)
    socket_server.message_recevied(handle_socket_message)
    socket_server.start()

    detector = EmotionDetector(
        detection_model_path="resources/face-detector.xml",
        emotion_model_path="resources/emotion-classifier.hdf5",
        image_offset=(20, 40)
    )

    detector.on_emotion_detected(handle_emotion)


if __name__ == "__main__":
    main()
