import socket
from utillities.logger import Logger

log = Logger(__name__)


class SocketClient():
    def __init__(self, host, port):
        self.client = socket.socket()
        self.client.connect((host, port))

    def send(self, message):
        self.client.send(message.encode())

    def close(self):
        self.client.close()