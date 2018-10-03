import socket
import asyncio
from threading import Thread


class SocketServer():
    def __init__(self, port, name):
        self.callbacks = []
        self.port = port
        self.name = name
        self.max_connections = 999
        self.is_running = False
        self.server = socket.socket()
        self.server.bind(('', self.port))
        self.server.listen(self.max_connections)

    def message_received(self, callback):
        self.callbacks.append(callback)

    def start(self):
        print('Starting server on port ' + str(self.port))
        self.is_running = True

        self.thread = Thread(target=self._start)
        self.thread.start()

    def close(self):
        self.is_running = False
        self.thread.is_alive = False
        self.server.close()

    def restart(self):
        self.close()
        self.start()

    def _on_message(self, message):
        for callback in self.callbacks:
            callback(message, self.name)

    def _start(self):
        print('Waiting for client to connect...')
        client, address = self.server.accept()
        print('new client connected: ' + str(client) + ', ' + str(address))

        while self.is_running:
            message = client.recv(1024).decode()
            self._on_message(message)
        
