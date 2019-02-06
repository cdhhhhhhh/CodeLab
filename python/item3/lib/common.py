from python.item3.conf import setting
import logging
import logging.config
import pickle
from python.item3.interface.student import *
from python.item3.interface.school import *
from python.item3.interface.teacher import *
from python.item3.core import src


def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger


def con_db():
    db_path = setting.DB_PATH
    with open(db_path, 'rb') as f:
        dic = pickle.loads(f.read())
    return dic


def fs_db(file):
    db_path = setting.DB_PATH
    with open(db_path, 'wb') as f:
        f.write(pickle.dumps(file))


def select(state, fn):
    flag = True
    while flag:
        number = input(src.print_text[state])
        if number == 'q':
            return
        else:
            fn(state, number)


def login(state):
    print('请登录')
    name = input('输入用户名')
    password = input('输入密码')
    if state == 'manage':
        if src.db_text[state]['name'] == name and src.db_text[state]['password'] == password:
            select('manage', handle)
        else:
            print('登录失败')
    elif state == 'teacher':

        pass
    elif state == 'student':

        pass


def register(state):
    name = input('输入用户名')
    if state == 'student':
        for i in src.db_text[state]:
            if name == i['name']:
                print('用户存在')
                return
        password = input('输入密码')
        print(list(list(i.keys()) for i in src.db_text['manage']['infos']['school']))
        school = input('输入关联学校')
        print(list(list(i[school].keys()) for i in src.db_text['manage']['infos']['school']))
        grade = input('输入关联年级')
        print('课程信息')
        course = list(i[school][grade] for i in src.db_text['manage']['infos']['school'])
        print(course)
        src.db_text[state].append({'name': name, 'password': password,'school':school, 'grade': grade, 'course': course[0]['course'],'score':0})
        print('注册成功')
        src.current_state['name'] = name
    elif name == 'manage':
        pass

    select(state, handle)


def handle(state, number):
    if state == 'student':
        if number == '1':
            # 选择学校
            Student.choose_school(src.db_text,src.current_state['name'])

        if number == '2':
            # 选择课程
            Student.choose_course(src.db_text,src.current_state['name'])

        if number == '3':
            # 查看成绩
            Student.print_grape(src.db_text,src.current_state['name'])

    if state == 'teacher':
        if number == '1':
            pass
        if number == '2':
            pass
        if number == '3':
            pass
        if number == '4':
            pass

    if state == 'manage':

        if number == '1':
            # 创建学校
            School.add_school(src.db_text)

        if number == '2':
            # 创建课程
            School.add_course(src.db_text)

        if number == '3':
            # 创建老师
            School.add_teacher(src.db_text)

    # 保存当前进度
            fs_db(src.db_text)
