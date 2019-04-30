from multiprocessing import Process
from threading import Thread
from time import *


def total_add(num):
    total = 0
    for i in range(num):
        total = total + i
    return total


def read_file():
    for i in range(10000):
        with open('./ticket', 'r') as fs:
            fs.read()


if __name__ == '__main__':
    timeStart = time()
    p_list = []
    q_list = []
    print('20进程和20线程进行累加10000000累加和10000次IO')
    for i in range(20):
        p = Process(target=total_add, args=(10000000,))
        p.start()
        p_list.append(p)
    for i in p_list:
        i.join()
    timeEnd = time()
    print('进程计算时间' + str(timeEnd - timeStart))
    timeStart = time()

    for i in range(20):
        q = Thread(target=total_add, args=(10000000,))
        q_list.append(q)
        q.start()
    for i in q_list:
        i.join()
    timeEnd = time()
    print('线程计算时间' + str(timeEnd - timeStart))

    p_list = []
    q_list = []
    timeStart = time()
    for i in range(20):
        p = Process(target=read_file)
        p.start()
        p_list.append(p)
    for i in p_list:
        i.join()
    timeEnd = time()
    print('进程IO时间' + str(timeEnd - timeStart))
    timeStart = time()

    for i in range(20):
        q = Thread(target=read_file)
        q_list.append(q)
        q.start()
    for i in q_list:
        i.join()
    timeEnd = time()
    print('线程IO时间' + str(timeEnd - timeStart))
