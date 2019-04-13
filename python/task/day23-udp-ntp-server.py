from socket import *
from time import ctime

ntpserver = socket(AF_INET, SOCK_DGRAM)
ntpserver.bind(('127.0.0.1', 8089))
print('开始ntf服务器')

while True:
    server_data, server_addr = ntpserver.recvfrom(1024)
    ntpserver.sendto(bytes('[%s] %s' % (ctime(), server_data), encoding='utf8'), server_addr)
    print('发送成功时间')
