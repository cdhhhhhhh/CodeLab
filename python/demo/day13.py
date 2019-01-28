import json

student_list = {}

with open('./text/student.json') as f:

     student_list = json.load(f)

class  CheckStudentGrade:

    def __init__(self, name, subject=''):
        self.name = name
        self.subject = subject

    def averagegrade(self):
        for k in student_list:
            print('%s平均分%s'%(k,(student_list[k]['Chinese']+student_list[k]['English']+student_list[k]['Math'])/3))

    def allstuent(self):
        for k in student_list:
            print(k,student_list[k])

    def studentgrade(self):
        print(self.name,student_list[self.name][self.subject])

    def delstudent(self):
        del student_list[self.name]
        print('删除成功%s'%self.name)

stu = CheckStudentGrade('foo','Chinese')
stu.averagegrade()
stu.allstuent()
stu.studentgrade()
stu.delstudent()
print(student_list)

