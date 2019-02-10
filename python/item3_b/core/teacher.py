from python.item3_b.interface import common
from python.item3_b.interface import teacher

select_list = [teacher.check_course,
               teacher.select_course,
               teacher.check_student,
               teacher.alter_score]


def run():
    print('''
    1、登录
    ''')
    number = input('请选择')
    if not (number == '1' or number == '2'):
        print('输入错误')
        return
    elif number == '1':
        common.login('teacher')

    while True:
        print('''
        0、查看课程
        1、选择课程
        2、查看学生成绩
        3、修改分数
        q、退出
        ''')
        number = input('请选择:')
        if number == 'q':
            break
        if int(number) < 4:
            select_list[int(number)]()
        else:
            print('输入错误')


if __name__ == '__main__':
    run()
