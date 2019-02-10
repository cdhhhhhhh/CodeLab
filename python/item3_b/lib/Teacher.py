class Teacher:
    def __init__(self):
        self.student_list = []
        self.teacher_info = {}
        self.course_list = []

    def course_is_exist(self, input_value):
        return input_value in self.course_list

    def find_student(self, input_value):
        student_name_list = [i['name'] for i in self.student_list]
        count = 0
        for i in student_name_list:
            if input_value == i:
                return count
            count += 1
        return ''

    def student_is_exist(self, input_value):
        return input_value in [i['name'] for i in self.student_list]
