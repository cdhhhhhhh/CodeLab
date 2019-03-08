from socket import *
from time import ctime

ntpserver = socket(AF_INET, SOCK_DGRAM)
ntpserver.bind(('127.0.0.1', 8089))
print('开始ntf服务器')

while True:
    data, addr = ntpserver.recvfrom(1024)
    ntpserver.sendto(bytes('[%s] %s' % (ctime(), data), encoding='utf8'), addr)
    print('发送成功时间')
