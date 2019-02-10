from python.item3_b.interface import manager, student, db
from python.item3_b.lib.School import *
from python.item3_b.conf import setting
import logging
import logging.config


def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger


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
        setting.CURRENT_USERNAME = name
        break


def register(status):
    while True:
        user_list = db.get_list(status)
        name = input('请输入用户名')
        if name not in user_list:
            password = input('请输入密码')
            if status == 'manager':
                setting.CURRENT_USERNAME = name
                manager.register_interface(name, password)
            else:
                setting.CURRENT_USERNAME = name
                student.register_interface(name, password)
                break
        else:
            print('用户名已存在')


def info_list():
    obj = School()
    obj.school_list = db.get_list('school')
    obj.teacher_list = db.get_list('teacher')
    for i in obj.school_list:
        obj.course_list.extend(db.get_info('school', i))

    return obj
