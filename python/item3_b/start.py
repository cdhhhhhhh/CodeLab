
from python.item3_b.core import manage,student,teacher

if __name__ == '__main__':
    while True:
        print('''
                1、管理者
                2、老师
                3、学生
                q、退出
                ''')
        i = input("请选择:")
        if i == '1':
            manage.run()
        elif i == '2':
            teacher.run()
        elif i == '3':
            student.run()
        elif i == 'q':
            break