from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from socket import *
from gevent import monkey;

monkey.patch_all()
import queue
import gevent

import time, os

max_process = os.cpu_count()
max_thread = 2000
server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8089))
server.listen(100)


def recv_msg(conn, i, q):
    print('>>>>>>>>>>>>')
    conn.recv(1024)
    conn.send(b'hello' + bytes(i, encoding='utf-8'))
    q.put('recv_msg')


def wait_time(q):
    time.sleep(2)
    q.put('wait_time')


def new_server(conn, addr):
    q = queue.Queue(1)
    total = 0
    print(addr)
    while True:
        r = gevent.spawn(recv_msg, conn, total, q)
        s = gevent.spawn(wait_time, q)
        gevent.joinall([r, s])
        # if q.get() == 'wait_time':
        #     r.dead()
        #     conn.close()
        #     return
        # else:
        #     s.dead()


def start_thread():
    t = ThreadPoolExecutor(max_thread)
    while True:
        conn, addr = server.accept()
        t.submit(new_server, conn, addr)


def start_process():
    p = ProcessPoolExecutor(max_workers=max_process)
    for i in range(1, 12):
        p.submit(start_thread)


if __name__ == '__main__':
    print('cpu数量:' + str(os.cpu_count()))
    start_process()
