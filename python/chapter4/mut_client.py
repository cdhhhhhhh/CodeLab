from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from socket import *

client = socket(AF_INET, SOCK_STREAM)


def conn_server():
    client.connect(('127.0.0.1', 8089))
    client.send(b'text')
    print(client.recv(1024))


if __name__ == '__main__':
    # t = ThreadPoolExecutor(500)
    # for i in range(500):
    #     t.submit(conn_server)
    conn_server()
