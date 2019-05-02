from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from socket import *
import gevent
import queue
import time, os

max_process = os.cpu_count()
max_thread = 2000
server = socket(AF_INET, SOCK_STREAM)

server.bind(('127.0.0.1', 8089))
server.listen(100)


def recv_msg(conn, i, q):
    try:
        conn.recv(1024)
        conn.send(b'hello' + str(i).encode('utf-8'))
        q.put('recv_msg')
    except ConnectionResetError:
        q.put('wait_time')


def wait_time(q):
    gevent.sleep(1)
    q.put('wait_time')


def new_server(conn, addr):
    q = queue.Queue(1)
    print(addr)
    total = 0
    while True:
        total = total + 1
        r = gevent.spawn(recv_msg, conn, total, q)
        # s = gevent.spawn(wait_time, q)
        gevent.wait([r], count=1)
        if q.get() == 'wait_time':
            gevent.killall([r])
            conn.close()
            print(addr)
            print('break')
            return
        else:
            # gevent.kill()
            pass

def start_thread():
    t = ThreadPoolExecutor()

    while True:
        conn, addr = server.accept()
        t.submit(new_server, conn, addr)


def start_process():
    p = ProcessPoolExecutor(max_workers=max_process)
    for i in range(12):
        p.submit(start_thread)


if __name__ == '__main__':
    print('cpu数量:' + str(os.cpu_count()))
    start_process()
