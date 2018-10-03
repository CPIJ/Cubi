from collections import namedtuple
from enum import Enum

Command = namedtuple('Command', ['action', 'parameter'])


class CommandType(Enum):
    set_led = 0,


def serialize_command(command):
    return f'{command.action}:{command.parameter}'


def parse_command(message):
    parts = message.split(':')
    if len(parts) == 2:
        return Command(parts[0], parts[1])
    else:
        return Command(parts[0], '')


def create_command(command_type, parameter):
    switch = {
        CommandType.set_led: "SET_LED"
    }

    action = switch.get(command_type, '')

    if not action:
        raise ValueError("Unkown command type")

    return Command(action, parameter)
