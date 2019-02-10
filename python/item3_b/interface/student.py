from python.item3_b.interface import db
from python.item3_b.conf import setting
from python.item3_b.lib.Student import *
from python.item3_b.interface import common



def student_info():
    obj = Student()

    obj.student_info = db.get_info('student', setting.CURRENT_USERNAME)
    if obj.student_info['school'] == '':
        obj.course_list = []
    else:
        obj.course_list = db.get_info('school', obj.student_info['school'])

    obj.school_list = db.get_list('school')
    common.get_logger(__name__).info('查看个人信息')
    return obj


def register_interface(name, password):
    obj = {'name': name, 'password': password, 'course': '', 'score': '', 'school': ''}
    db.save('student', obj, name)
    common.get_logger(__name__).info('注册成功')


def select_school():
    obj = student_info()
    school_list = obj.school_list

    print('可选择')
    print(school_list)
    school = input('输入选择学校')
    if obj.school_is_exist(school):
        obj.student_info['school'] = school
        db.save('student', obj.student_info, setting.CURRENT_USERNAME)
        common.get_logger(__name__).info('选择学校成功')
    else:
        print('学校不存在')


def select_course():
    obj = student_info()
    course__list = obj.course_list
    if obj.student_info['school'] == '':
        print('请先选择学校')
        return
    print('可选择')
    print(course__list)
    course = input('输入选择课程')
    if obj.course_is_exist(course):
        obj.student_info['course'] = course
        obj.student_info['score'] = ''
        db.save('student', obj.student_info, setting.CURRENT_USERNAME)
        common.get_logger(__name__).info('选择课程成功')

    else:
        print('课程不存在')


def check_score():
    print(db.get_info('student', setting.CURRENT_USERNAME))
    common.get_logger('db').info('查看个人成绩')

if __name__ == '__main__':
    setting.CURRENT_USERNAME = 'stu1'
    #select_school()
    check_score()
