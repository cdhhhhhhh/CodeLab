import requests

arr = []

for i in range(500000, 700000):
    r = requests.get('http://cp-tools.cn/auth/verify?uid=%s' % i)
    if r.json()['msg'] != '未购买':
        arr.append(r.json())

with open('./text/muke', 'w+') as f:
    f.write(str(arr))
