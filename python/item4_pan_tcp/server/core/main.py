from interface import main_interface
from lib import common

fun_dic = {
    'register': main_interface.register_interface,
    'login': main_interface.login_interface,
    'add_vip': main_interface.add_vip_interface,
    'renew_vip': main_interface.renew_vip_interface,
    'check_vip': main_interface.check_vip_interface,
    'upload_file': main_interface.upload_file_interface,
    'check_list': main_interface.check_list_interface,
    'download_file': main_interface.download_file_interface

}


def run():
    main_interface.creat_server_interface()
    main_interface.main_server.conn = common.bind_server(main_interface.main_server.ip,
                                                         main_interface.main_server.port).accept()[0]
    while True:
        main_interface.main_server.rev_msg()
        handler_type = main_interface.main_server.type
        if handler_type in fun_dic.keys():
            fun_dic[handler_type]()
