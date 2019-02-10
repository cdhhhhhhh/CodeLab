from python.item3_b.interface import common
from python.item3_b.interface import school
from python.item3_b.conf import setting

select_list = [school.add_school,
               school.add_course,
               school.add_teacher]


def run():
    print('''
    1、登录
    2、注册
    ''')
    number = input('请选择')
    if not (number == '1' or number == '2'):
        print('输入错误')
        return
    elif number == '1':
        common.login('manager')
    elif number == '2':
        common.register('manager')

    while True:
        print('''
        0、创建学校
        1、创建课程
        2、创建老师
        q、退出
        ''')
        number = input('请选择:')
        if number == 'q':
            setting.CURRENT_USERNAME = ''
            break
        if int(number) < 3:
            select_list[int(number)]()
        else:
            print('输入错误')


if __name__ == '__main__':
    run()
