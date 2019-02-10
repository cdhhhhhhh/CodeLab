from python.item3_b.interface import db, common


def add_school():
    obj = common.info_list()

    print('现在的学校')
    print(obj.school_list)
    school = input('输入添加学校')

    if obj.school_is_exist(school):
        print('学校已存在')
    else:
        db.save('school', [], school)


def add_course():
    obj = common.info_list()

    print(obj.course_list)
    course = input('输入添加课程')
    if obj.course_is_exist(course):
        print('课程已存在')
        return
    print(obj.school_list)
    school = input('输入关联学校')
    if obj.school_is_exist(school):
        temp = db.get_info('school', school)
        temp.append(course)
        print(temp)
        db.save('school', temp, school)
    else:
        print('学校不存在')


def add_teacher():
    obj = common.info_list()
    print(obj.teacher_list)
    teacher = input('输入老师姓名')
    if obj.teacher_is_exist(teacher):
        print('老师已存在')
        return
    print(obj.school_list)
    school = input('输入关联学校')
    password = input('输入密码')
    if obj.school_is_exist(school):
        db.save('teacher', {'password': password, 'school': school}, teacher)
    else:
        print('学校不存在')


if __name__ == '__main__':
    # add_school()
    #add_course()
    add_teacher()
    pass
