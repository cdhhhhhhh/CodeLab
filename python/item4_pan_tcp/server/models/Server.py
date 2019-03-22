from lib import common


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.msg = {}
        self.type = ''
        self.conn = None

    def send_msg(self, msg):
        common.send_msg(self.conn, msg)

    def rev_msg(self):
        info = common.rev_msg(self.conn)
        self.type = info['type']
        self.msg = info['msg']
