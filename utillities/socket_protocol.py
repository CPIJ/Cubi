from collections import namedtuple
from enum import Enum

Command = namedtuple('Command', ['action', 'parameter'])


class CommandType(Enum):
    set_led = 0,
    set_mode = 1,
    exit = 2
    enable_color = 3,
    disable_color = 4,
    set_level = 5


def serialize_command(command):
    return f'{command.action}:{command.parameter}'


def parse_command(message):
    parts = message.split(':')
    if len(parts) == 2:
        return Command(parts[0], parts[1])
    else:
        return Command(parts[0], '')


def create_command(command_type, parameter=''):
    switch = {
        CommandType.set_led: "SET_LED",
        CommandType.set_mode: "SET_MODE",
        CommandType.exit: "EXIT",
        CommandType.enable_color: "ENABLE_COLOR",
        command_type.disable_color: "DISABLE_COLOR",
        command_type.set_level: "SET_LEVEL"
    }

    action = switch.get(command_type, '')

    if not action:
        raise ValueError("Unkown command type")

    return Command(action, parameter)
