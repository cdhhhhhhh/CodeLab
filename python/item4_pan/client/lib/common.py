import socket
import json
from conf import setting


def send_msg(msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = bytes(json.dumps(msg), encoding='utf-8')
    client.sendto(msg, (setting.server_ip, setting.server_port))
    res, server_addr = client.recvfrom(1024)
    return json.loads(str(res, encoding='utf-8'))


def register(usrname, passowrd):
    msg = {
        'type': 'register',
        'msg': {
            'username': usrname,
            'password': passowrd
        }
    }
    return send_msg(msg)


def login(usrname, passowrd):
    msg = {
        'type': 'login',
        'msg': {
            'username': usrname,
            'password': passowrd
        }
    }
    return send_msg(msg)


def login_auth(username):
    if username == '':
        print('请先等登录')
        return False
    else:
        return True


if __name__ == '__main__':
    send_msg({'type': 'test'})
