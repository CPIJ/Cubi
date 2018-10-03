from collections import namedtuple
import json

SocketConfig = namedtuple('SocketConfig', ['host', 'port'])

def get_server_config(name):
    with open('config/server-config.json') as file:
        socket_config = json.load(file)
        return SocketConfig(socket_config[name]["host"], socket_config[name]["port"])

LED_SERVER = get_server_config("LED_SERVER")
LOGIC_SERVER = get_server_config("LOGIC_SERVER")
IO_SERVER = get_server_config("IO_SERVER")
