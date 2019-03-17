from lib import common


class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.user_list = {}
        self.vip_date = ''
        self.file_list = []

    def add_vip_date(self, server, msg):
        common.send_db(server, 'modify_user_vip', msg)

    def check_vip(self, server, msg):
        common.send_db(server, 'user_info', msg)

    def add_file(self):
        pass
