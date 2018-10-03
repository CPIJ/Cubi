from collections import namedtuple

Command = namedtuple('Command', ['action', 'parameter'])

def parse_command(message):
    parts = message.split(':')
    assert len(parts) == 2

    return Command(parts[0], parts[1])