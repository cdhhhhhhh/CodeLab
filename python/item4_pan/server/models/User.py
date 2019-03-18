from lib import common


class User:
    def __init__(self, vip_date, file_list):
        self.username = ''
        self.password = ''
        self.user_list = {}
        self.vip_date = vip_date
        self.file_list = file_list

    def add_vip_date(self, server, msg):
        common.send_db(server, 'modify_user_vip', msg)

    def check_vip(self, server, msg):
        common.send_db(server, 'user_info', msg)

    def get_upload_file_info(self, file_obj, db_server):
        has_vip = '1' if self.vip_date != '' else '0'
        has_file = '1' if file_obj.md5 in [i['md5'] for i in self.file_list] else '0'
        speed = file_obj.vip_speed if self.vip_date != '' else file_obj.com_speed
        return {'type': '1', 'msg': {'has_vip': has_vip, 'db_server': db_server, 'has_file': has_file,
                                     'speed': speed}}

    def get_download_file_info(self, file_obj, db_server):
        has_vip = '1' if self.vip_date != '' else '0'
        speed = file_obj.vip_speed if self.vip_date != '' else file_obj.com_speed

        return {
            'type': '1',
            'msg': {
                'has_vip': has_vip,
                'speed': speed,
                'db_server': db_server,
                'file_size': file_obj.file_size,
                'md5': file_obj.md5,
                'file_name': file_obj.file_name
            }
        }
