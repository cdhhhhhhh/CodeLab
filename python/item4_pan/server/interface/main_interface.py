from models.Server import *
from models.User import *
from lib import common
from conf import setting

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
    user_obj = User()
    if main_server.msg['vip_date'] == '':
        user_obj.add_vip_date(main_server, client_msg)
        main_server.send_msg({'type': '1', 'msg': 'add vip suss'}, client_addr)
    else:
        main_server.send_msg({'type': '0', 'msg': 'add vip fail'}, client_addr)


def renew_vip_interface():
    client_addr = main_server.server_addr
    client_msg = main_server.msg
    common.send_db(main_server, 'user_info', main_server.msg)
    user_obj = User()
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
