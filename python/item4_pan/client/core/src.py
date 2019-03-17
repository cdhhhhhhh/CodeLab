from lib import common
from lib import vip

current_name = ''


def login():
    global current_name
    username = input('输入用户名')
    password = input('输入密码')
    rev_msg = common.login(username, password)
    if rev_msg['type'] == '1':
        current_name = username
        print('登陆成功')
    else:
        print(rev_msg['msg'])


def register():
    username = input('输入用户名')
    password = input('输入密码')
    conf_password = input('确认密码')
    if password == conf_password:
        rev_msg = common.register(username, password)
        if rev_msg['type'] == '1':
            print('注册成功')
        else:
            print('用户名存在')
    else:
        print('密码不一致')


def member():
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
            fun_dic[flg](current_name)


def download():
    pass


def upload():
    pass


def logout():
    global current_name
    current_name = ''
    print('退出成功！')


def run():
    fun_dic = {
        '1': login,
        '2': register,
        '3': upload,
        '4': download,
        '5': member,
        '6': logout
    }

    while True:
        print('''
                 1 登录
                 2 注册
                 3 上传
                 4 下载
                 5 会员
                 6 注销
                 ''')
        choice = input('输入选择')
        if choice in fun_dic.keys():
            fun_dic[choice]()
        else:
            print('输入错误')
