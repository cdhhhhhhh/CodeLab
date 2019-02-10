from python.item3_b.interface import db
from python.item3_b.conf import setting
from python.item3_b.lib.Teacher import *
from python.item3_b.interface import common


def teacher_info():
    obj = Teacher()
    obj.teacher_info = db.get_info('teacher', setting.CURRENT_USERNAME)
    obj.course_list = db.get_info('school', obj.teacher_info['school'])

    for i in db.get_list('student'):
        if db.get_info('student', i)['course'] == obj.teacher_info['course']:
            obj.student_list.append(db.get_info('student', i))
    return obj


def check_course():
    print('当前课程' + db.get_info('teacher', setting.CURRENT_USERNAME)['course'])
    common.get_logger(__name__).info('查看课程')

def select_course():
    obj = teacher_info()
    course_list = obj.course_list
    print(course_list)
    course = input('输入选择课程')
    if obj.course_is_exist(course):
        obj.teacher_info['course'] = course
        db.save('teacher', obj.teacher_info, setting.CURRENT_USERNAME)
        common.get_logger(__name__).info('选择学校成功')
    else:
        print('课程不存在')


def check_student():
    obj = teacher_info()
    print(obj.student_list)
    common.get_logger(__name__).info('查看学生列表')


def alter_score():
    obj = teacher_info()
    print(obj.student_list)
    student_name = input('输入修改学生姓名')
    if obj.student_is_exist(student_name):
        save_student = obj.student_list[obj.find_student(student_name)]
        print(save_student)
        score = input('输入修改成绩')

        save_student['score'] = score

        db.save('student', save_student, student_name)
        common.get_logger(__name__).info('修改成绩成功')
    else:
        print('学生不存在')


if __name__ == '__main__':
    setting.CURRENT_USERNAME = 'tom'
    # select_course()
    # check_student()
    # check_course()
    alter_score()
