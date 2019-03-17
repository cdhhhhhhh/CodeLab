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
    print(msg)
    all_user = handler.read_user()
    if handler.mkdir(msg['username']):
        all_user[msg['username']] = {
            'password': msg['password'],
            'file': [],
            'vip': ''
        }
        handler.write_user(all_user)
        db_server.send_msg({'type': '1', 'msg': 'register suss'}, '')
    else:
        db_server.send_msg({'type': '0', 'msg': 'register fail'}, '')


def check_user():
    msg = db_server.msg
    all_user = handler.read_user()
    if msg['username'] in all_user.keys():
        if msg['password'] == all_user[msg['username']]['password']:
            db_server.send_msg({'type': '1', 'msg': 'login suss'}, '')
        else:
            db_server.send_msg({'type': '0', 'msg': 'password fail'}, '')
    else:
        db_server.send_msg({'type': '0', 'msg': 'not username '}, '')


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
