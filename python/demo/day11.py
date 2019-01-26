'''
1、文件内容如下,标题为:姓名,性别,年纪,薪资

albert male 18 3000
james male 38 30000
林志玲 female 28 20000
新垣结衣 female 28 10000

要求:
从文件中取出每一条记录放入列表中,
列表的每个元素都是{'name':'albert','sex':'male','age':18,'salary':3000}的形式

2 根据1得到的列表,取出薪资最高的人的信息

3 根据1得到的列表,取出最年轻的人的信息

4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式

5 根据1得到的列表,过滤掉名字以a开头的人的信息

6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 5 7...)

7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值
'''

with open('./text/day11') as f:
    dic = [{'name':line.split(' ')[0],'sex':line.split(' ')[1],'age':line.split(' ')[2],'salary':line.split(' ')[3].replace('\n','')}  for line in f ]
    print(dic)
    print(max(dic,key=lambda x:int(x['salary'])))
    print(min(dic,key=lambda x:int(x['age'])))
    print(list(map(lambda x:x['name'].title(),dic)))
    print(list(filter(lambda x:x['name'][0]!='a',dic)))

def foo(f,s):
    print(f)
    if f >10000:
        return

    if s == 0:
        f=1
        s=1
    else:
        temp = f
        f = s + f
        s = temp
    foo(f,s)
#foo(0,1)

l=[1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]

def bar(l):
    for i in l:
        if type(i) == list:
            bar(i)
        else:
            print(i)

bar(l)