'''
1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作

2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
'''
import os
import re
import types


# 第一道题

def ma_fs(name, pattern, text='', text_r=''):
    name_temp = './' + name + '.swap'
    name = './' + name
    with open(name, 'r') as fs:

        if pattern == 'r':
            for line in fs:
                print(line)
        if pattern == 'w+':
            with open(name_temp, 'w+') as fs_temp:
                for line in fs:
                    line = line.replace(text, text_r)
                    fs_temp.write(line)
    if pattern == 'w+':
        os.remove(name)
        os.rename(name_temp, name)


def re_fs():
    print(os.listdir('./'))
    text_name = input('输入修改的文件名')
    if (text_name in os.listdir('./')):
        ma_fs('task.txt', 'r')
        text = input('输入修改信息')
        text_r = input('输入修改为')
        ma_fs(text_name, 'w+', text, text_r)
    else:
        print('文件不存在')
    return


# re_fs ()
# 第二道题
def check_str(str):
    print('空白个数%s' % list(str).count(' '))
    print('数字个数%s' % len(re.compile(r'\d').findall(str)))
    print('字母个数%s' % len(re.compile(r'[a-zA-Z]').findall(str)))
    print('其他个数%s' % len(re.compile(r'[^a-zA-Z0-9]').findall(str.replace(' ', ''))))


# check_str('da s d3@2332 3--')
# 第三道题
def check_long(obj):
    if type(obj) == str:
        print(len(list(obj)) > 5)
        return len(list(obj)) > 5
    elif type(obj) == list:
        print(len(obj) > 5)
        return len(obj) > 5
    elif type(obj) == dict:
        print(len(list(obj.keys())) > 5)
        return len(list(obj.keys())) > 5
    else:
        print('输入正确的格式')


# check_long({'aa':'aa','aaa':'aaa'})
# check_long('aaa')
# check_long([1,2,3,4])
# 第四道题
def check_list(list):
    if (len(list) > 2):
        print(list[0:2])
        return list[0:2]
    else:
        print('少于数量')


# check_list([1,2,3,4])
# 第五道题
def check_odd(item):
    print(item[::2])
    return item[::2]


# check_odd((1,2,3,4))
# 第六道题
def check_values(dict):
    temp = {}
    for key, word in dict.items():
        temp[key] = word[0:2]
    print(temp)
    return temp


dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# check_values(dic)
