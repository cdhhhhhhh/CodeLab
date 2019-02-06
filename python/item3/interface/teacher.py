class Teacher:
    @classmethod
    def choose_course(cls, db, name):
        school = ''
        for i in db['teacher']:
            if name == i[0]:
                school = i[1]

        for i in db['manage']['infos']['school']:
            if school in list(i.keys()):
                courser = input('输入选择课程')
                #清楚以前课的关联
                for j in i[school]:
                    if i[school][j]['teacher'] == name:
                        i[school][j]['teacher'] = ''
                #关联当前的课
                for j in i[school]:
                    if i[school][j]['course'] == courser:
                        i[school][j]['teacher'] = name

    @classmethod
    def print_stu(cls, db, name):
        for i in db['student']:
            print(i)

    @classmethod
    def print_course(cls, db, name):
        school = ''
        for i in db['teacher']:
            if name == i[0]:
                school = i[1]

        for i in db['manage']['infos']['school']:
            if school in list(i.keys()):
                print(list(list(i.values())))

    @classmethod
    def alter_score(cls, db):
        grade = input('输入修改课程')
        score = input('输入修改分数')
        for i in db['student']:
            if i['grade'] == grade:
                i['score'] = score
