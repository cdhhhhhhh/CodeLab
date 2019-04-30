from socket import *
from threading import Thread


def con_serve():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8089))
    while

if __name__ == '__main__':
    for i in range(10):
        c = Thread(target=con_serve)
        c.start()
