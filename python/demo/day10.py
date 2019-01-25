'''
1、将names=['albert','james','kobe','kd']中的名字全部变大写

2、将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度

3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）

4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
6、文件shopping.txt内容如下
mac,20000,3
lenovo,3000,10
tesla,1000000,10
chicken,200,1
（1）求总共花了多少钱？

（2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]

（3）求单价大于10000的商品信息,格式同上

'''

#第一题
names=['albert','james','kobe','kd']
name = [names[i].upper() for i in range(0,len(names))]
#print(name)


#第二题
names=['albert','jr_shenjing','kobe','kd']
name = [len(item) for item in names if not item.endswith('shenzhen')]
#print(name)

#第三题
with open('day10.txt',encoding='utf-8') as f:
    print(max(len(line) for line in f))

#第四题
with open('day10.txt', encoding='utf-8') as f:
    print(sum(len(line) for line in f))


#第六题
with open('./text/day10',encoding='utf-8') as f:
    info = [[line[:line.find(',')],line[line.find(',')+1:line.rfind(',')],line[line.rfind(',')+1:].replace('\n','')] for line in f]
    print(sum(int(i[2]) for i in info))
    print([{'name':i[0],'priice':i[1],'count':i[2]} for i in info])
    print([{'name':i[0],'priice':i[1],'count':i[2]} for i in info if int(i[1])>10000])
