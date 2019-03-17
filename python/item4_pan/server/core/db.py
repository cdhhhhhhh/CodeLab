from interface import db_interface

func_dic = {
    'add_user': db_interface.add_user,
    'check_user': db_interface.check_user,
    'upload_file': db_interface.upload_file,
    'download_file': db_interface.download_file,
    'add_vip': db_interface.add_vip,
    'check_file': db_interface.check_file,
    'check_vip': db_interface.check_vip
}


def run():
    while True:
        handler_type = db_interface.creat_server_interface()
        if handler_type in func_dic.keys():
            func_dic[handler_type]()
