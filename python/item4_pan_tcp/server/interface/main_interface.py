from models.Server import *
from models.User import *
from models.File import *
from lib import common
from conf import setting
from core import db

db_server = (setting.db_ip, setting.db_port)

# 全局实例
main_server = None


def creat_server_interface():
    # 生成唯一一个实例方便处理
    global main_server
    main_server = Server(setting.server_ip, setting.server_port)


def register_interface():
    recv_msg = db.run('add_user', main_server.msg)
    main_server.send_msg(recv_msg)


def login_interface():
    client_msg = main_server.msg
    recv_msg = db.run('user_list')
    user_list = recv_msg['msg']
    if client_msg['username'] in user_list.keys():
        if client_msg['password'] == user_list[client_msg['username']]['password']:
            main_server.send_msg({'type': '1', 'msg': 'login suss'})
        else:
            main_server.send_msg({'type': '0', 'msg': 'password fail'})
    else:
        main_server.send_msg({'type': '0', 'msg': 'not username '})


def add_vip_interface():
    recv_msg = db.run('user_info', main_server.msg)
    user_obj = User(recv_msg['msg']['vip_date'])
    if main_server.msg['vip_date'] == '':
        user_obj.add_vip_date(main_server.msg)
        main_server.send_msg({'type': '1', 'msg': 'add vip suss'})
    else:
        main_server.send_msg({'type': '0', 'msg': 'add vip fail'})


def renew_vip_interface():
    recv_msg = db.run('user_info', main_server.msg)
    user_obj = User(recv_msg['msg']['vip_date'])
    if main_server.msg['vip_date'] != '':
        main_server.msg['vip_date'] = str(int(main_server.msg['vip_date']) + int(main_server.msg['vip_date']))
        user_obj.add_vip_date(main_server.msg)
        main_server.send_msg({'type': '1', 'msg': 'add vip date suss'})
    else:
        main_server.send_msg({'type': '0', 'msg': 'add vip date fail'})


def check_vip_interface():
    recv_msg = User().check_vip(main_server.msg)
    main_server.send_msg({'type': '1', 'msg': recv_msg['msg']['vip_date']})


def upload_file_interface():
    file_obj = File(main_server.msg['file_name'], main_server.msg['file_size'], main_server.msg['md5'])
    recv_msg = db.run('user_info', main_server.msg)
    use_obj = User(recv_msg['msg']['vip_date'], recv_msg['msg']['file'])
    db.run('modify_user_file', main_server.msg)
    main_server.send_msg(use_obj.get_upload_file_info(file_obj))
    if use_obj.get_upload_file_info(file_obj)['msg']['has_file'] == '0':
        db.run('upload_file', (main_server, use_obj.get_upload_file_info(file_obj)))


def check_list_interface():
    recv_msg = db.run('user_info', main_server.msg)
    main_server.send_msg({'type': '1', 'msg': recv_msg['msg']})


def download_file_interface():
    recv_msg = db.run('user_info', main_server.msg)['msg']
    file_obj = None
    for i in recv_msg['file']:
        if i['file_name'] == main_server.msg['file_name']:
            file_obj = File(i['file_name'], i['file_size'], i['md5'])
    user_obj = User(recv_msg['vip_date'], recv_msg['file'])
    if main_server.msg['file_name'] in [i['file_name'] for i in recv_msg['file']]:
        main_server.send_msg(user_obj.get_download_file_info(file_obj))
        db.run('download_file', (main_server, user_obj.get_download_file_info(file_obj)))
    else:
        main_server.send_msg({'type': '0', 'msg': ' file not exist'})
