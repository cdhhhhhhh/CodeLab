from interface import db_interface

func_dic = {
    'add_user': db_interface.add_user,
    'user_list': db_interface.user_list,
    'upload_file': db_interface.upload_file,
    'download_file': db_interface.download_file,
    'user_info': db_interface.user_info,
    'modify_user_vip': db_interface.modify_user_vip,
    'modify_user_file': db_interface.modify_user_file
}


def run(fun_type, msg=None):
    return func_dic[fun_type](msg)
