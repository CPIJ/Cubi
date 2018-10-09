from argparse import ArgumentParser
from config.socket_config import get_server_config
from utillities.classes.socket_server import SocketServer

servers = []


def close_server(server_name):
    global servers

    server = next(filter(lambda server: server.name == server_name, servers))

    if server is not None:
        server.close()


def on_message(message, sender):
    if message == "exit":
        sender.close()
    else:
        print('{name}: {message}'.format(name=sender.name, message=message))


def create_server(server_name):
    config = get_server_config(server_name)
    return SocketServer(config.port, server_name)


def main():
    global servers

    parser = ArgumentParser()
    parser.add_argument('--servers', nargs='+', required=True)
    args = parser.parse_args()

    servers = map(lambda name: create_server(name), args.servers)

    for server in servers:
        server.message_received(on_message)
        server.start()


if __name__ == '__main__':
    main()
