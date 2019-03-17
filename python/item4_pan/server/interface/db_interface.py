from db import handler
from models.Server import *
from conf import setting

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
    print(msg)

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


def upload_file():
    pass


def download_file():
    pass


def add_vip():
    pass


def check_file():
    pass


def check_vip():
    pass
