from multiprocessing import Process
from socket import *
import random


def deal_client(conn, addr):
    captha = random.randint(1000, 9999)
    print(addr)
    conn.send(bytes(str(captha), encoding='utf8'))
    data = conn.recv(1024)
    if bytes.decode(data) == str(captha):
        conn.send(b'suss')
    else:
        conn.send(b'fail')
    conn.close()


def main():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8095))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        client = Process(target=deal_client, args=(conn, addr))
        client.start()
        conn.close()


if __name__ == '__main__':
    main()
