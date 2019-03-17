from lib import common
from models.Server import *
from conf import setting

main_server = None
db_server = (setting.db_ip, setting.db_port)


def creat_server_interface():
    global main_server
    main_server = Server(setting.server_ip, setting.server_port)
    main_server.rev_msg()
    return main_server.type


def register_interface():
    msg = {
        'type': 'add_user',
        'msg': main_server.msg
    }
    main_server.send_msg(msg, db_server)
    client_server = main_server.server_addr
    main_server.rev_msg()
    main_server.send_msg('', client_server)


def login_interface():
    msg = {
        'type': 'check_user',
        'msg': main_server.msg
    }
    main_server.send_msg(msg, db_server)
    client_server = main_server.server_addr
    main_server.rev_msg()
    main_server.send_msg('', client_server)


