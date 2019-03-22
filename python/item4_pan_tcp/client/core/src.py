from lib import common
from lib import vip
from lib import manger_ftp

current_info = {'username': ''}


def login_view():
    global current_info
    username = input('输入用户名').strip()
    password = input('输入密码').strip()
    common.login(username, password)
    rev_msg = common.recv_msg()
    if rev_msg['type'] == '1':
        current_info['username'] = username
        print('登陆成功')
    else:
        print(rev_msg['msg'])


def register_view():
    username = input('输入用户名').strip()
    password = input('输入密码').strip()
    conf_password = input('确认密码').strip()
    if password == conf_password:
        common.register(username, password)
        rev_msg = common.recv_msg()
        if rev_msg['type'] == '1':
            print('注册成功')
        else:
            print('用户名存在')
    else:
        print('密码不一致')


@common.login_auth(current_info)
def member_view():
    fun_dic = {
        '1': vip.add_vip,
        '2': vip.renew_vip,
        '3': vip.check_vip_date
    }
    while True:
        flg = input('''
        1.办理会员
        2.续费
        3.查看到期时间
        ''')
        if flg in fun_dic.keys():
            fun_dic[flg](current_info['username'])
        else:
            return


@common.login_auth(current_info)
def download_view():
    manger_ftp.download_file(current_info['username'])


@common.login_auth(current_info)
def upload_view():
    manger_ftp.upload_file(current_info['username'])


@common.login_auth(current_info)
def check_file():
    common.check_file_list(current_info['username'])


@common.login_auth(current_info)
def logout():
    global current_info
    current_info['username'] = ''
    print('退出成功！')


def run():
    fun_dic = {
        '1': login_view,
        '2': register_view,
        '3': upload_view,
        '4': download_view,
        '5': check_file,
        '6': member_view,
        '7': logout
    }

    while True:
        print('''
                 1 登录
                 2 注册
                 3 上传
                 4 下载
                 5 文件  
                 6 会员
                 7 注销
                 ''')
        choice = input('输入选择')
        if choice in fun_dic.keys():
            fun_dic[choice]()
        else:
            print('输入错误')
