from interface import db_interface

func_dic = {
    'add_user': db_interface.add_user,
    'user_list': db_interface.user_list,
    'upload_file': db_interface.upload_file,
    'download_file': db_interface.download_file,
    'add_vip': db_interface.add_vip,
    'file_list': db_interface.check_file,
    'user_info': db_interface.user_info,
    'modify_user_vip':db_interface.modify_user_vip
}


def run():
    while True:
        handler_type = db_interface.creat_server_interface()
        if handler_type in func_dic.keys():
            func_dic[handler_type]()
