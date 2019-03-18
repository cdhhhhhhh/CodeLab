import socket
import json
from conf import setting

db_server = (setting.db_ip, setting.db_port)


def bind_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ip, port))
    return server


def send_msg(msg, server_addr, ip, port):
    bind_server(ip, port).sendto(bytes(json.dumps(msg), encoding='utf-8'), server_addr)


def rev_msg(ip, port, size=2048):
    server_data, server_addr = bind_server(ip, port).recvfrom(size)
    return json.loads(str(server_data, encoding='utf-8')), server_addr


def rev_file(size=2024, ip=db_server[0], port=db_server[1]):
    server_data, server_addr = bind_server(ip, port).recvfrom(size)
    return server_data


def send_file(msg, server_addr, ip, port):
    bind_server(ip, port).sendto(msg, server_addr)


def send_db(server, type, msg):
    msg = {
        'type': type,
        'msg': msg
    }
    server.send_msg(msg, db_server)
    server.rev_msg()
