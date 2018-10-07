import utillities.colors as colors
from config.socket_config import get_server_config
from utillities.classes.socket_client import SocketClient
from utillities.socket_protocol import Command, CommandType
from utillities.models.emotion import get_level
from utillities.logger import Logger
from time import sleep

test_mode = True
led_server_commands = ["SET_COLOR", "TRAIN"]
io_server_commands = ["SET_MODE"]
log = Logger(__name__)
level = 1


def get_color(emotion_name):
    emotions = get_level(level)
    try:
        emotion = next((filter(lambda emotion: emotion.name ==emotion_name, [x[1] for x in emotions.items()])))
        return emotion.color
    except:
        print(f'{emotion_name} does not exist')
        return (0, 0, 0)


def handle_io_command(command, server):
    if command.action == "SET_MODE":
        server.send(command.serialize())


def train(emotion_name, server):
    color = get_color(emotion_name.lower())
    delay = 0.8

    for i in range(3):
        print(3 - i)
        color_cmd = Command.create(CommandType.set_color, color)
        server.send(color_cmd.serialize())

        sleep(delay)

        black_cmd = Command.create(CommandType.set_color, '(0,0,0)')
        server.send(black_cmd.serialize())

        sleep(delay)

    result = input("Was the emotion correct? [Y/N]: ").lower()
    result_color = colors.get('green' if result == "y" else 'red')
    result_command = Command.create(CommandType.set_color, result_color)
    server.send(result_command.serialize())


def handle_led_command(command, server):
    if command.action == "SET_COLOR":
        try:
            eval(command.parameter)
        except:
            emotion_name = command.parameter.lower()
            color = get_color(emotion_name)
            command.parameter = str(color)

        server.send(command.serialize())
    elif command.action == "TRAIN":
        train(command.parameter, server)


def handle_command(command, servers):
    if command.action == "EXIT":
        for name in servers:
            servers[name].close()

        return False

    elif command.action in led_server_commands:
        handle_led_command(command, servers["led_server"])
    elif command.action in io_server_commands:
        handle_io_command(command, servers["io_server"])

    return True


def start_servers():
    io_server_config = get_server_config("IO_SERVER", is_test=test_mode)
    led_server_config = get_server_config("LED_SERVER", is_test=test_mode)

    io_server = SocketClient(io_server_config.host, io_server_config.port)
    led_server = SocketClient(led_server_config.host, led_server_config.port)

    return {
        "led_server": led_server,
        "io_server": io_server
    }


def main():
    servers = start_servers()

    while True:
        command = Command.parse(input("Enter Command: "))
        was_succesful = handle_command(command, servers)

        if not was_succesful:
            break


if __name__ == "__main__":
    main()
