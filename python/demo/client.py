import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 数据报协议
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)

client.sendto(bytes(json_str, encoding="utf8"), ('127.0.0.1', 8081))
