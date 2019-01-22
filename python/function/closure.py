'''
1 编写函数，（函数执行的时间是随机的）

2 编写装饰器，为函数加上统计时间的功能

3 编写装饰器，为函数加上认证的功能

4 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）
    要求：
        登录成功一次，后续的函数都无需再输入用户名和密码
    注意：
        从文件中读出字符串形式的字典，可以用
        eval('{"name":"albert","password":"123"}')转成字典格式

5 编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录

6 编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果

7 为题目五编写装饰器，实现缓存网页内容的功能：
具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，
否则，就去下载，然后存到文件中
扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中

8 还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，
在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作

9 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
注意：时间格式的获取
'''
import time
import random
flag = False
login_time = 0
def auth(func):
    def auth(*args,**kwargs):
        dic = {}
        global flag
        if not flag:
            with open('./closure') as fs:
                dic = eval(fs.read())
                username = input('username')
                password = input('password')
                if time.time()-login_time < 0.0000000000001:
                    if username == dic['name'] and password == dic['password']:
                        flag = True
                        print('login')
                        func(*args, **kwargs)
                    else:
                        print('falid login')
                else:
                    pass
    return auth

def random_num(func):
    def temp():
        num = random.randint(1, 10)
        print('%s秒'%num)
        time.sleep(num)
        func()

    return temp

def overtime_num(func):
    global login_time
    def temp(*args,**kwargs):
        t1 = time.time()
        res = func(*args,**kwargs)
        t2 = time.time()
        login_time = t2-t1
        return res
    return temp


@auth
def random_time():
    print(time.strftime('%Y-%m-%d %X'))

@auth
@overtime_num
def test_data():
    pass

#test_data()


#第七题
import requests
import os
cache_file='cache.txt'
def make_cache(func):
    def wrapper(*args,**kwargs):
        if not os.path.exists(cache_file):
            with open(cache_file,'w'):pass

        if os.path.getsize(cache_file):
            with open(cache_file,'r',encoding='utf-8') as f:
                res=f.read()
        else:
            res=func(*args,**kwargs)
            with open(cache_file,'w',encoding='utf-8') as f:
                f.write(res)
        return res
    return wrapper

@make_cache
def get(url):
    return requests.get(url).text

print(get('https://www.baidu.com'))

#第八题
route_dic={}

def make_route(name):
    def deco(func):
        route_dic[name]=func
    return deco
@make_route('select')
def func1():
    print('select')

@make_route('insert')
def func2():
    print('insert')

@make_route('update')
def func3():
    print('update')

@make_route('delete')
def func4():
    print('delete')

print(route_dic)

#题目九
import time
import os

def logger(logfile):
    def deco(func):
        if not os.path.exists(logfile):
            with open(logfile,'w'):pass

        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            with open(logfile,'a',encoding='utf-8') as f:
                f.write('%s %s run\n' %(time.strftime('%Y-%m-%d %X'),func.__name__))
            return res
        return wrapper
    return deco

@logger(logfile='aaaaaaaaa.log')
def index():
    print('index')

index()