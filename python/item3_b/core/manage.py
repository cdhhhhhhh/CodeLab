select_list = {

}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、创建学校
        4、创建课程
        6、创建老师
        8、查看现有信息
        q、退出
        ''')
        number = input('请选择:').replace(' ', '')
        if number == 'q':
            break
        if number in select_list:
            select_list[number]()


if __name__ == '__main__':
    run()
