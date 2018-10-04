import utillities.colors as colors
from utillities.socket_protocol import Command
from utillities.classes.socket_server import SocketServer
from config.socket_config import LED_SERVER as server_config
from ledstrip import LedStrip
from utillities.logger import Logger

strip = LedStrip()
strip.start()
log = Logger(__name__)

def handle_message(message, sender):
    command = Command.parse(message)

    if not command.parameter:
        log.error('Empty parameter for command: ' + command.serialize())
        return
        
    if command.action == "SET_COLOR":
        color = eval(command.parameter)
        strip.transition_to(color, 100)

    elif command.action == "EXIT":
        strip.transition_to(colors.get("black"), 100)
        server.restart()

    else:
        log.error('Unown command: ' + command.parameter)

if __name__ == "__main__":
    server = SocketServer(server_config.port, "LED_SERVER")
    server.message_received(handle_message)
    server.start()
