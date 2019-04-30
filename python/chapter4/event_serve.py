from threading import Event, current_thread, Thread
import time
from socket import *

event = Event()


def check():
    print('%s 正在检测服务是否正常....' % current_thread().name)
    time.sleep(5)
    event.set()


def connect(conn, addr):
    num = 0
    print(addr)
    while event.is_set() and num < 4:
        conn.send(b'connect fail')
        num = num + 1
    conn.send(b'connect suss')


if __name__ == '__main__':
    c1 = Thread(target=check)
    c1.start()
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8089))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        client = Thread(target=connect, args=(conn, addr))
        client.start()
        conn.close()
