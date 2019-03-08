from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('输入data ')
    if not data:
        break
    client.sendto(bytes(data,encoding='utf-8'), ('127.0.0.1',8089))
    data, ADDR = client.recvfrom(1024)
    print(data)
