from interface import main_interface

fun_dic = {
    'register': main_interface.register_interface,
    'login': main_interface.login_interface,
    'add_vip': main_interface.add_vip_interface,
    'renew_vip': main_interface.renew_vip_interface,
    'check_vip': main_interface.check_vip_interface,
    'upload_file': main_interface.upload_file_interface,
    'upload_file_ok':main_interface.upload_file_ok_interface,
    'check_list':main_interface.check_list_interface,
    'download_file':main_interface.download_file_interface

}


def run():
    while True:
        handler_type = main_interface.creat_server_interface()
        if handler_type in fun_dic.keys():
            fun_dic[handler_type]()
