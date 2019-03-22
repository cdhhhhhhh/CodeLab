from lib import common


def add_vip(username):
    add_date = input('输入办理时长')
    common.send_msg({'type': 'add_vip', 'msg': {'username': username, 'vip_date': add_date}})
    recv_msg = common.recv_msg()
    if recv_msg['type'] == '1':
        print('办理成功')
    else:
        print('已办理请续费')


def renew_vip(username):
    add_date = input('输入增加时长')
    common.send_msg({'type': 'renew_vip', 'msg': {'username': username, 'vip_date': add_date}})
    recv_msg = common.recv_msg()
    if recv_msg['type'] == '1':
        print('增加成功')
    else:
        print('请办理先办理会员')


def check_vip_date(username):
    common.send_msg({'type': 'check_vip', 'msg': {'username': username}})
    recv_msg = common.recv_msg()
    print('剩余'+recv_msg['msg']+'天')
