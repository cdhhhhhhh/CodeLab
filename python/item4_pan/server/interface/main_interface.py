from models.Server import *
from models.User import *
from models.File import *
from lib import common
from conf import setting

db_server = (setting.db_ip, setting.db_port)

# 全局实例
main_server = None


def creat_server_interface():
    # 生成唯一一个实例方便处理
    global main_server
    main_server = Server(setting.server_ip, setting.server_port)
    main_server.rev_msg()
    return main_server.type


def register_interface():
    client_addr = main_server.server_addr
    common.send_db(main_server, 'add_user', main_server.msg)

    main_server.send_msg('', client_addr)


def login_interface():
    client_addr = main_server.server_addr
    client_msg = main_server.msg
    common.send_db(main_server, 'user_list', main_server.msg)

    user_list = main_server.msg
    if client_msg['username'] in user_list.keys():
        if client_msg['password'] == user_list[client_msg['username']]['password']:
            main_server.send_msg({'type': '1', 'msg': 'login suss'}, client_addr)
        else:
            main_server.send_msg({'type': '0', 'msg': 'password fail'}, client_addr)
    else:
        main_server.send_msg({'type': '0', 'msg': 'not username '}, client_addr)


def add_vip_interface():
    client_addr = main_server.server_addr
    client_msg = main_server.msg
    common.send_db(main_server, 'user_info', main_server.msg)
    user_obj = User(main_server.msg['vip_date'])
    if main_server.msg['vip_date'] == '':
        user_obj.add_vip_date(main_server, client_msg)
        main_server.send_msg({'type': '1', 'msg': 'add vip suss'}, client_addr)
    else:
        main_server.send_msg({'type': '0', 'msg': 'add vip fail'}, client_addr)


def renew_vip_interface():
    client_addr = main_server.server_addr
    client_msg = main_server.msg
    common.send_db(main_server, 'user_info', main_server.msg)
    user_obj = User(main_server.msg['vip_date'])
    if main_server.msg['vip_date'] != '':
        client_msg['vip_date'] = str(int(client_msg['vip_date']) + int(main_server.msg['vip_date']))
        user_obj.add_vip_date(main_server, client_msg)
        main_server.send_msg({'type': '1', 'msg': 'add vip date suss'}, client_addr)
    else:
        main_server.send_msg({'type': '0', 'msg': 'add vip date fail'}, client_addr)


def check_vip_interface():
    client_addr = main_server.server_addr
    User().check_vip(main_server, main_server.msg)
    main_server.send_msg({'type': '1', 'msg': main_server.msg['vip_date']}, client_addr)


def upload_file_interface():
    client_addr = main_server.server_addr
    client_msg = main_server.msg
    file_obj = File(client_msg['file_name'], client_msg['file_size'], client_msg['md5'])
    common.send_db(main_server, 'user_info', main_server.msg)
    use_obj = User(main_server.msg['vip_date'], main_server.msg['file'])
    main_server.send_msg(use_obj.get_upload_file_info(file_obj, db_server), client_addr)


def upload_file_ok_interface():
    client_addr = main_server.server_addr

    common.send_db(main_server, 'modify_user_file', main_server.msg)
    main_server.send_msg({'type': '1', 'msg': 'upload ok'}, client_addr)


def check_list_interface():
    client_addr = main_server.server_addr
    common.send_db(main_server, 'user_info', main_server.msg)
    main_server.send_msg({'type': '1', 'msg': main_server.msg}, client_addr)


def download_file_interface():
    client_addr = main_server.server_addr
    client_msg = main_server.msg
    common.send_db(main_server, 'user_info', main_server.msg)
    file_obj = None
    for i in main_server.msg['file']:
        if i['file_name'] == client_msg['file_name']:
            file_obj = File(i['file_name'], i['file_size'], i['md5'])
    user_obj = User(main_server.msg['vip_date'],main_server.msg['file'])
    if client_msg['file_name'] in [i['file_name'] for i in main_server.msg['file']]:
        main_server.send_msg(user_obj.get_download_file_info(file_obj,db_server), client_addr)
    else:
        main_server.send_msg({'type': '0', 'msg': ' file not exist'}, client_addr)
