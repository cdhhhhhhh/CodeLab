class Student:

    @classmethod
    def choose_school(cls, db, name):
        print(list(list(i.keys()) for i in db['manage']['infos']['school']))
        school = input('输入选择学校')
        for i in db['student']:
            if i['name'] == name:
                i['school'] = school
                i['grade'] = ''
                i['course'] = ''
                i['score'] = 0
        print('选择学校成功' + school)

    @classmethod
    def choose_course(cls, db, name):
        for i in db['student']:
            if i['name'] == name:
                print(list(list(j[i['school']].values()) for j in db['manage']['infos']['school'])[0])
                course = input('输入选择课程')
                grade = input('输入选择班级')
                i['grade'] = grade
                i['course'] = course
                i['score'] = 0
        print('修改成功')

    @classmethod
    def print_grape(cls, db, name):
        for i in db['student']:
            if i['name'] == name:
                print(i['grade'] + '成绩')

