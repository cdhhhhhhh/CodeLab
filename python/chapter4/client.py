from socket import *
from multiprocessing import Process


def register(i):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8089))
    chapter = client.recv(1024)
    print('验证码' + bytes.decode(chapter))
    client.send(chapter)
    print('用户' + str(i) + '>>>>>>>>>>>' + bytes.decode(client.recv(1024)))
    client.close()


def main():
    for i in range(30):
        c = Process(target=register, args=(i,))
        c.start()


if __name__ == '__main__':
    main()
