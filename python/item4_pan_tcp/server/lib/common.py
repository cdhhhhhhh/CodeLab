import socket
import json
from conf import setting

db_server = (setting.db_ip, setting.db_port)


def bind_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    return server


def send_msg(conn, msg):
    conn.send(bytes(json.dumps(msg), encoding='utf-8'))


def rev_msg(conn, size=5555):
    server_data = conn.recv(size)
    return json.loads(str(server_data,encoding='utf-8'))


