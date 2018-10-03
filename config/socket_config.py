from collections import namedtuple
import json

SocketConfig = namedtuple('SocketConfig', ['host', 'port'])

with open('config/server-config.json') as file:
    socket_config = json.load(file)

LED_SERVER = SocketConfig(socket_config["LED_SERVER"]["host"], socket_config["LED_SERVER"]["port"])
LOGIC_SERVER = SocketConfig(socket_config["LOGIC_SERVER"]["host"], socket_config["LOGIC_SERVER"]["port"])
IO_SERVER = SocketConfig(socket_config["IO_SERVER"]["host"], socket_config["IO_SERVER"]["port"])