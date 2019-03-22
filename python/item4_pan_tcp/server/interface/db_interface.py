from db import handler
from models.User import *
from models.File import *
import time


def add_user(msg):
    all_user = handler.read_user()
    if handler.mkdir(msg['username']):
        all_user[msg['username']] = {
            'password': msg['password'],
            'file': [],
            'vip_date': ''
        }
        handler.write_user(all_user)
        return {'type': '1', 'msg': 'register ok'}
    else:
        return {'type': '0', 'msg': 'register fail'}


def user_info(msg):
    all_user = handler.read_user()
    return {'type': '1', 'msg': all_user[msg['username']]}


def user_list(msg):
    all_user = handler.read_user()
    return {'type': '1', 'msg': all_user}


def modify_user_vip(msg):
    all_user = handler.read_user()
    all_user[msg['username']]['vip_date'] = msg['vip_date']
    handler.write_user(all_user)
    return {'type': '1', 'msg': 'add vip date'}


def modify_user_file(msg):
    all_user = handler.read_user()

    all_user[msg['username']]['file'].append(
        {'file_name': msg['file_name'], 'file_size': msg['file_size'], 'md5': msg['md5']})
    handler.write_user(all_user)
    return


def upload_file(obj_msg):
    server = obj_msg[0]
    msg = obj_msg[0].msg
    print(obj_msg[1])
    file_obj = File(msg['file_name'], msg['file_size'], msg['md5'])
    with open('/Users/cuidaohan/item/lab/python/item4_pan_tcp/server/db/' + msg['username'] + '/' + file_obj.file_name,
              'wb') as f:
        current_size = 0
        speed_size = int(obj_msg[1]['msg']['speed'])
        while current_size < int(file_obj.file_size):
            print('接收数据' + str(current_size))
            current_size = current_size + speed_size
            f.write(server.conn.recv(speed_size))


def download_file(obj_msg):
    msg = obj_msg[1]['msg']
    server = obj_msg[0]
    print(msg)
    file_size = msg['file_size']
    username = server.msg['username']
    file_name = msg['file_name']
    upload_speed = int(msg['speed'])
    with open('/Users/cuidaohan/item/lab/python/item4_pan_tcp/server/db/' + username + '/' + file_name, 'rb') as f:
        current_size = 0
        while current_size < int(file_size):
            print(current_size)
            current_size = current_size + upload_speed
            server.conn.send(f.read(upload_speed))
            if current_size > int(file_size):
                print('完成')
                server.conn.send(f.read(upload_speed - (current_size - file_size)))
                return


if __name__ == '__main__':
    add_user({'username': 'dasd', 'password': 'a'})
