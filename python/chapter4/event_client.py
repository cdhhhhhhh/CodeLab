from socket import *
import time

if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8089))
    while True:
        client.send(b'connect')
        data = client.recv(1024)
        time.sleep(1)
        print(data)
        if data == b'connect fail' or data == b'connect suss':
            client.close()
            break
    client.close()
