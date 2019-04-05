import time
import random
from multiprocessing import Process, JoinableQueue


def consumer(name, q):
    while True:
        res = q.get()
        if res is None:
            break
        time.sleep(random.randint(1, 3))
        print('\033[46m消费者===》%s 吃了 %s\033[0m' % (name, res))
        q.task_done()


def producer(name, q, food):
    for i in range(5):
        time.sleep(random.randint(1, 2))
        res = '%s%s' % (food, i)
        q.put(res)
        print('\033[45m生产者者===》%s 生产了 %s\033[0m' % (name, res))


if __name__ == '__main__':
    q = JoinableQueue()

    p1 = Process(target=producer, args=('Albert主厨', q, '新疆大盘鸡'))
    p2 = Process(target=producer, args=('厨神', q, '扬州烧鹅'))
    p3 = Process(target=producer, args=('主厨的小迷弟', q, '南京回锅肉'))

    c1 = Process(target=consumer, args=('孙悟空', q))
    c2 = Process(target=consumer, args=('猪八戒', q))
    c1.daemon = True  # 子进程变成守护进程
    c2.daemon = True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    # 确定生产者确实生产完毕
    p1.join()
    p1.join()
    p1.join()

    # 生产者生产完毕之后，拿到队列中肯定有还有数据，直到这个数据量变为0，q.join()这行代码才算是运行完毕
    q.join()
    # q.join()一旦结束就意味着队列确实为空，消费者已经确实把数据都取干净了。
    print('主进程结束')
