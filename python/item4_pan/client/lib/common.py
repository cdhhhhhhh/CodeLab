import socket
import json
from conf import setting

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_msg(msg, server_info=(setting.server_ip, setting.server_port)):
    msg = bytes(json.dumps(msg), encoding='utf-8')
    client.sendto(msg, server_info)
    res, server_addr = client.recvfrom(2048)
    return json.loads(str(res, encoding='utf-8'))


def send_file(msg, server_info):
    client.sendto(msg, server_info)


def rev_file(size):
    client_data, client_addr = client.recvfrom(size)
    return client_data


def check_file_list(username):
    recv = send_msg({'type': 'check_list', 'msg': {'username': username}})
    for i in recv['msg']['file']:
        print('文件名==>>' + i['file_name'] + '-----------' + str(i['file_size']) + 'b')


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


def login_auth(user):
    def auth(func):
        def wrapper(*args, **kwargs):
                if user['username'] == '':
                    print('请注册')
                else:
                    func(*args, **kwargs)

        return wrapper
    return auth


if __name__ == '__main__':
    send_msg({'type': 'test'})
