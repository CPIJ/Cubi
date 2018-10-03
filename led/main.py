import utillities.colors as colors
import utillities.socket_protocol as socket_protocol
from utillities.classes.socket_server import SocketServer
from config.socket_config import LED_SERVER as server_config
from ledstrip import LedStrip

strip = LedStrip()
strip.start()


def handle_message(message, sender):
    command = socket_protocol.parse_command(message)

    if command.action == "SET_COLOR":
        color = eval(command.parameter)
        strip.transition_to(color, 100)

    if command.action == "EXIT":
        server.close()
        strip.transition_to(colors.get("black"), 100)


if __name__ == "__main__":
    server = SocketServer(server_config.port, "LED_SERVER")
    server.message_received(handle_message)
    server.start()
