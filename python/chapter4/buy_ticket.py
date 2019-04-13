from multiprocessing import Process, Lock
import time
import random

mutex = Lock()


def production_ticket():
    with open('./ticket', 'w') as fs:
        ticket_list = []
        for i in range(10):
            ticket_list.append('ticket_number' + str(i))
        fs.write(' '.join(ticket_list))


def check_ticket(num, lock):
    print('用户' + str(num) + '查看票')
    time.sleep(random.randint(1, 5))
    buy_ticket(num, lock)


def buy_ticket(num, lock):
    lock.acquire()
    with open('./ticket', 'r') as rs:
        ticket_list = (rs.read()).split()
        print(ticket_list)
        if bool(ticket_list):
            with open('./ticket', 'w') as ws:
                ticket_list.pop()
                ws.write(' '.join(ticket_list))
            print('用户' + str(num) + '购票成功')

        else:
            print('用户'+str(num)+'购票失败')

    lock.release()


if __name__ == '__main__':
    p = Process(target=production_ticket)
    p.start()
    p.join()
    for i in range(100):
        c = Process(target=check_ticket, args=(i, mutex))
        c.start()

