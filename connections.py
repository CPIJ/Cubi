import socket
from threading import Thread


class SocketServer():
    def __init__(self, port):
        self.callbacks = []
        self.port = port
        self.max_connections = 999
        self.is_running = False
        pass

    def message_recevied(self, callback):
        self.callbacks.append(callback)

    def on_message(self, message):
        for callback in self.callbacks:
            callback(message)

    def start(self):
        self.is_running = True

        thread = Thread(target=self._start)
        thread.start()

        return thread

    def stop(self):
        self.is_running = False

    def _start(self):
        server = socket.socket()
        server.bind(('', self.port))
        server.listen(self.max_connections)

        print('Waiting for client to connect...')
        client, address = server.accept()
        print(f'new client connected: {client}, {address}')

        while self.is_running:
            message = client.recv(1024).decode()
            self.on_message(message)


class SocketClient():
    def __init__(self, host, port):
        self.client = socket.socket()
        self.client.connect((host, port))

    def send(self, message):
        self.client.send(message.encode())

    def close(self):
        self.client.close()
