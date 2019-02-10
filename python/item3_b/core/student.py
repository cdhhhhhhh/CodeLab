from python.item3_b.interface import common
from python.item3_b.interface import student
from python.item3_b.conf import setting
select_list = [student.select_school,
               student.select_course,
               student.check_score]


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
        common.login('student')
    elif number == '2':
        common.register('student')

    while True:
        print('''
        0、选择学校
        1、选择课程
        2、查看分数
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
