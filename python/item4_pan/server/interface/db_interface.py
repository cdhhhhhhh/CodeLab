from db import handler
from models.Server import *
from models.User import *
from models.File import *
from conf import setting
import time

db_server = None


def creat_server_interface():
    global db_server
    db_server = Server(setting.db_ip, setting.db_port)
    db_server.rev_msg()
    return db_server.type


def add_user():
    msg = db_server.msg
    all_user = handler.read_user()
    if handler.mkdir(msg['username']):
        all_user[msg['username']] = {
            'password': msg['password'],
            'file': [],
            'vip_date': ''
        }
        handler.write_user(all_user)
        db_server.send_msg({'type': '1', 'msg': 'register suss'}, '')
    else:
        db_server.send_msg({'type': '0', 'msg': 'register fail'}, '')


def user_info():
    msg = db_server.msg
    all_user = handler.read_user()
    db_server.send_msg({'type': '1', 'msg': all_user[msg['username']]}, '')


def user_list():
    all_user = handler.read_user()
    db_server.send_msg({'type': '1', 'msg': all_user}, '')


def modify_user_vip():
    msg = db_server.msg
    all_user = handler.read_user()
    all_user[msg['username']]['vip_date'] = msg['vip_date']
    handler.write_user(all_user)
    db_server.send_msg({'type': '1', 'msg': 'add vip date'}, '')


def modify_user_file():
    msg = db_server.msg
    all_user = handler.read_user()

    all_user[msg['username']]['file'].append(
        {'file_name': msg['file_name'], 'file_size': msg['file_size'], 'md5': msg['md5']})
    handler.write_user(all_user)
    # db_server.send_msg({'type': '1', 'msg': all_user[msg['username']]}, '')
    db_server.send_msg('', '')


def upload_file():
    msg = db_server.msg
    file_obj = File(msg['file_name'], msg['file_size'], msg['md5'])
    db_server.send_msg('', '')
    with open('/Users/cuidaohan/item/lab/python/item4_pan/server/db/' + msg['username'] + '/' + file_obj.file_name,
              'wb') as f:
        current_size = 0
        speed_size = int(db_server.msg['speed'])
        while current_size < int(file_obj.file_size):
            print('接收数据' + str(current_size))
            current_size = current_size + speed_size
            f.write(common.rev_file(speed_size))
            if current_size > int(file_obj.file_size):
                print('接收数据完成')
                f.write(common.rev_file(speed_size - (current_size - int(file_obj.file_size))))


def download_file():
    msg = db_server.msg
    client_server = db_server.server_addr
    print(client_server)
    file_size = msg['file_size']
    username = msg['username']
    file_name = msg['file_name']
    upload_speed = int(msg['speed'])
    db_server.send_msg('', '')
    with open('/Users/cuidaohan/item/lab/python/item4_pan/server/db/' + username + '/' + file_name, 'rb') as f:
        current_size = 0
        while current_size < int(file_size):
            time.sleep(1)
            print(current_size)
            current_size = current_size + upload_speed
            common.send_file(f.read(upload_speed), client_server, db_server.ip, db_server.port)
            if current_size > int(file_size):
                time.sleep(1)
                print('完成')
                common.send_file(f.read(upload_speed - (current_size - file_size)), client_server, db_server.ip,
                                 db_server.port)
