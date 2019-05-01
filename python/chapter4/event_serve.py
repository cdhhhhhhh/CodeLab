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
    while not event.is_set():
        num = num + 1
        conn.recv(1024)
        if num > 3:
            conn.send(b'connect fail')
            conn.close()
            return
        conn.send(b'connect again')
    conn.send(b'connect suss')
    conn.close()


def main():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8089))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        s = Thread(target=connect, args=(conn, addr))
        s.start()


if __name__ == '__main__':
    c1 = Thread(target=check)
    c1.start()
    main()
