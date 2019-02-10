from python.item3_b.interface import db
from python.item3_b.interface import manager, student, school
from python.item3_b.lib.School import *


def login(status):
    count = 0
    while True:
        if count == 3:
            print('输入次数过多')
            exit()
        name = input('请输入用户名')
        user_list = db.get_list(status)
        if name not in user_list:
            print('用户名不存在')
            continue
        password = input('请输入密码')
        if password != db.get_info(status, name)['password']:
            print('密码错误')
            count += 1
            continue
        break


def register(status):
    while True:
        user_list = db.get_list(status)
        name = input('请输入用户名')
        if name not in user_list:
            password = input('请输入密码')
            if status == 'manager':
                manager.register_interface(name, password)
            else:
                pass
        else:
            print('用户名已存在')


def info_list():
    obj = School()
    obj.school_list = db.get_list('school')
    obj.teacher_list = db.get_list('teacher')
    for i in obj.school_list:
        obj.course_list.extend(db.get_info('school', i))

    return obj
