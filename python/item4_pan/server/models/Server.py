from lib import common


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_addr = ()
        self.msg = {}
        self.type = ''

    def send_msg(self, msg, server_addr):
        if msg == '':
            msg = {'type': self.type, 'msg': self.msg}
        if server_addr == '':
            server_addr = self.server_addr
        common.send_msg(msg, server_addr, self.ip, self.port)

    def rev_msg(self):
        info, self.server_addr = common.rev_msg(self.ip, self.port)
        self.type = info['type']
        self.msg = info['msg']
