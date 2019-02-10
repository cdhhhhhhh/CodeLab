class School:

    def __init__(self):
        self.school_list = []
        self.course_list = []
        self.teacher_list = []

    def school_is_exist(self, input_value):
        return input_value in self.school_list

    def course_is_exist(self, input_value):
        return input_value in self.course_list

    def teacher_is_exist(self, input_value):
        return input_value in self.teacher_list
