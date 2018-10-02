from connections import SocketServer, SocketClient
from emotion_detector import EmotionDetector


def handle_emotion(emotion, kwargs):
    client = kwargs['client']
    client.send(f'Color:{str(emotion.color)}')


def handle_socket_message(message):
    switch = {
        "SET_MODE:CONVERSATION": lambda: print('Zet em naar conversation'),
        "SET_MODE:TRAINING": lambda: print('Zet em naar training'),
        "EXIT": lambda: print('Zet em uit'),
    }

    func = switch.get(message, lambda: print('Unknown command'))

    func()

def main():
    ledstrip_client = SocketClient('192.168.250.1', 8000)

    server = SocketServer(9000)
    server.message_recevied(handle_socket_message)
    server.start()

    detector = EmotionDetector(
        detection_model_path="resources/face-detector.xml",
        emotion_model_path="resources/emotion-classifier.hdf5",
        image_offset=(20, 40)
    )

    detector.on_emotion_detected(handle_emotion, client=ledstrip_client)
    detector.start()


if __name__ == "__main__":
    main()
