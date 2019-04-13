'''
1、自定义函数模拟range(1,7,2)

2、模拟管道，实现功能:tail -f access.log | grep '404'

3、编写装饰器，实现初始化协程函数的功能

4、实现功能：grep  -rl  'python'  /etc

5、Python语言 实现八皇后问题
'''

#第一题
def r_range(start,end,space=1):
    while start < end:
        try:
            yield start
            start+=space
        except StopIteration:
            break

obj = r_range(1,7,2)

print(next(obj))
print(next(obj))
print(next(obj))

#第二题
import time
def tail(filepath):
    with open (filepath,'rb') as fs:
        fs.seek(0,2)
        while True:
            line = fs.readline()
            if line:
                yield line
            else:
                time.sleep(2)

def grep(patten,lines):
    for line in lines:
        line = line.decode('utf-8')
        if patten in line:
            yield line

for line in grep('404',tail('file.log')):
    print(line,end='')

with open('file.log','a',encoding='utf-8') as fs:
    fs.write('404\n')



#题目三
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper
@init
def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)

g=eater('albert')
g.send('蒸羊羔')



#题目四
import os
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def search(target):
    while True:
        filepath=yield
        g=os.walk(filepath)
        for dirname,_,files in g:
            for file in files:
                abs_path=r'%s\%s' %(dirname,file)
                target.send(abs_path)
@init
def opener(target):
    while True:
        abs_path=yield
        with open(abs_path,'rb') as f:
            target.send((f,abs_path))
@init
def cat(target):
    while True:
        f,abs_path=yield
        for line in f:
            res=target.send((line,abs_path))
            if res:
                break
@init
def grep(pattern,target):
    tag=False
    while True:
        line,abs_path=yield tag
        tag=False
        if pattern.encode('utf-8') in line:
            target.send(abs_path)
            tag=True
@init
def printer():
    while True:
        abs_path=yield
        print(abs_path)

