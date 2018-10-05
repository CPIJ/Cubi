import socket
import asyncio
from threading import Thread
from utillities.logger import Logger

log = Logger(__name__)


class SocketServer():
    def __init__(self, port, name):
        self.callbacks = []
        self.port = port
        self.name = name
        self.max_connections = 999
        self.is_running = False
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('', self.port))
        self.server.listen(self.max_connections)

    def message_received(self, callback):
        self.callbacks.append(callback)

    def start(self):
        self.is_running = True
        self.thread = Thread(target=self._start)
        self.thread.start()
        log.info('Server started on port ' + str(self.port))

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

    def _on_new_client(self, client, address):
        log.info('New client connected: ' + str(address))
        while True:
            message = client.recv(1024).decode()

            if not message:
                log.info('Client ' + str(address) + ' disconnected')
                break

            log.info(message)

            self._on_message(message)

        client.close()

    def _start(self):
        while self.is_running:
            try:
                client, address = self.server.accept()
                Thread(target=self._on_new_client, args=(client, address)).start()
            except:
                log.info('Server shutting down.')
                break
