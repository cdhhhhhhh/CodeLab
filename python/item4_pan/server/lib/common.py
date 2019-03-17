import socket
import json


def bind_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ip, port))
    return server


def send_msg(msg, server_addr, ip, port):
    bind_server(ip, port).sendto(bytes(json.dumps(msg), encoding='utf-8'), server_addr)


def rev_msg(ip, port, size=1024):
    server_data, server_addr = bind_server(ip, port).recvfrom(size)
    return json.loads(str(server_data, encoding='utf-8')), server_addr
