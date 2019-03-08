from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('输入data ')
    if not msg:
        break
    client.sendto(bytes(msg, encoding='utf-8'), ('127.0.0.1', 8089))
    client_data, client_arr = client.recvfrom(1024)

    print(client_data)
