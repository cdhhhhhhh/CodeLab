from python.item3.lib import common

current_state = {}
logger = common.get_logger(__name__)
db_text = common.con_db()
print_text = {
    'student':
        '''
        1.选择学校
        2.选择课程
        3.查看分数
        q.退出登录
        ''',
    'teacher':
        '''
        1.选择课程
        2.查看课程
        3.查看学生
        4.修改分数
        q.退出
          ''',
    'manage':
        '''
        1.创建学校
        2.创建课程
        3.创建老师
        q.退出
        '''
}
print(db_text)
db_text = {'student': [
    {'name': 'stu1', 'password': 'stu1', 'school': 'shanghai', 'grade': 'class1', 'course': 'AI', 'score': 0}],
           'teacher': [['toto', 'shanghai'], ['kula', 'shanghai'], ['roti', 'NewYork'], ['yure', 'NewYork']],
           'manage': {'user': {'admin': 'admin'}, 'infos': {'school': [{'shanghai': {
               'class1': {'course': 'AI', 'teacher': ''}, 'class2': {'course': 'Python', 'teacher': 'toto'}}}],
                                                            'course': [['AI', '40000', '4'], ['Python', '6000', '6'],
                                                                       ['ML', '9000', '8']]}}}

while True:
    select_view = input('选择登录身份')

    if select_view == '学生':
        number = input('1.登录 2.注册')
        if number == '1':
            common.login('student')
        if number == '2':
            common.register('student')
    if select_view == '老师':
        common.login('teacher')

    if select_view == '管理':
        number = input('1.登录 2.注册')
        if number == '1':
            common.login('manage')
        if number == '2':
            common.register('manage')
