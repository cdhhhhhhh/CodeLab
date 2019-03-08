from python.item4_qq.clinet import lib


def run():
    while True:
        tag1 = input('''
         1.注册
         2.登录
        ''')
        if tag1 == '1':
            lib.register()
        elif tag1 == '2':
            lib.login()

