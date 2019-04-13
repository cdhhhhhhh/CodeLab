class DeepSharePeople:
    school = 'deepshare'

    def __init__(self, name):
        self.name = name
        self.course = []


class DeepShareTeacher(DeepSharePeople):

    def add_course(self,name,price):
        self.course.append([name,price])

    def watch_course(self):
        print('老师====>'+self.name)
        for i in self.course:
            print(i)


class DeepShareStudent(DeepSharePeople):

    def add_course(self,name):
        self.course.append(name)

    def watch_course(self):
        print('学生====>'+self.name)
        for i in self.course:
            print(i)


stu = DeepShareStudent('stu')
stu.add_course('math')
tea = DeepShareTeacher('tea')
tea.add_course('math',200)
stu.watch_course()
tea.watch_course()