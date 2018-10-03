from collections import namedtuple
from enum import Enum


class Command():
    def __init__(self, action, parameter):
        self.action = action
        self.parameter = parameter

    def serialize(self):
        return str(self.action) + ':' + str(self.parameter)

    @staticmethod
    def parse(message):
        parts = message.split(':')

        if len(parts) == 2:
            return Command(parts[0], parts[1])
        else:
            return Command(parts[0], '')

    @staticmethod
    def create(command_type, parameter=''):
        switch = {
                CommandType.set_color: "SET_COLOR",
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



class CommandType(Enum):
    set_color = 0,
    set_mode = 1,
    exit = 2
    enable_color = 3,
    disable_color = 4,
    set_level = 5