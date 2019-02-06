class School:
    @classmethod
    def add_school(cls, db):
        flag = True
        name = input('输入创建学校')
        temp = {}
        while flag:
            grade = input('输入创建班级')
            print(db['manage']['infos']['course'])
            course = input('输入关联课程')
            print(db['teacher'])
            teacher = input('输入关联老师')
            temp[grade] ={'course': course, 'teacher': teacher}
            if input('退出按q') == 'q':
                db['manage']['infos']['school'].append({name: temp})
                flag = False

    @classmethod
    def add_teacher(cls, db):
        teacher = input('输入老师姓名')
        school = input('输入关联学校')
        db['teacher'].append([teacher, school])

    @classmethod
    def add_course(cls, db):
        course = input('输入课程')
        price = input('输入价格')
        period = input('输入周期')
        db['manage']['infos']['course'].append([course, price, period])
