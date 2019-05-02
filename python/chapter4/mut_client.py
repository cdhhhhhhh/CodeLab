from concurrent.futures import ThreadPoolExecutor, wait, ProcessPoolExecutor
from multiprocessing import Process
from socket import *
import time
import random

def conn_server():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8089))
    for i in range(random.randint(1, 2)):
        # time.sleep(random.randint(1, 2))
        client.send(b'connect')
        print(client.recv(1024))
    client.close()


if __name__ == '__main__':

    t_list = []
    for i in range(2000000):
        t = Process(target=conn_server)
        t.start()
        t_list.append(t)

    for i in t_list:
        i.join()
