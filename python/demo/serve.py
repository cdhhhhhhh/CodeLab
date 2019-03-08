import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 数据报协议
server.bind(('127.0.0.1', 8081))

while True:
    client_data, client_addr = server.recvfrom(1024)
    print(json.loads(str(client_data, encoding="utf8"))['name'])
