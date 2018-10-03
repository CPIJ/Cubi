from collections import namedtuple

SocketConfig = namedtuple('SocketConfig', ['ip', 'port'])

LED_SERVER = SocketConfig('192.168.250.2', 8000)
