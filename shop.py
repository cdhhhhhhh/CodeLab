import os
goods = [
	{'apple':10},
	{'mac':100}
]
user = []
total = 0;
money = 1000;
flagU = False
flagP = False
goods_list = {'apple':0,'mac':0}
banName = []
numPassword = 0;
username = ''	

with open('./text.txt') as fs:
	for line in fs:
		user.append({line.split('|')[0]:line.split('|')[1].replace('\n','')});
with open('./baname.txt') as fs:
	for line in fs:
			banName.append(line)

while True:
	if not flagU:
		username = input('输入用户名')
		if username in banName:
			print('该用户加入黑名单')
			exit()
		for item in user:
			if username in item.keys():
				flagU = True
				flagP = True
				break;
		if not flagU:
			print('用户名不存在')
	if flagP:
		password = input('输入密码')
		for item in user:
			if password in item.values():
				flagP = False
				break;
		if flagP:
			numPassword = numPassword + 1
			print('密码错误%s次'%numPassword)
		if numPassword == 3:
			username = username +'\n'
			with open('./baname.txt','a') as fs:
				fs.write(username)
			print('输出密码次数过多，加入黑名单')
			exit()
	if not flagP and flagU:	
		print('登陆成功')
		break;
def find_goods(flag):
	for item in goods:
		if flag in item.keys():
			return item
	print('没有该商品')
	return 'null';
	
while True:
	flag = input('输入商品,q退出,t当前购买商品?')
	nowTotal = 0;
	num = 0
	if flag=='q':
		exit()
	if flag =='t':
		for key,value in goods_list.items():
			print('%s>>>>%s'%(key,value))
			print('当前金额%s'%total)
			continue	
	flag = find_goods(flag)
	if flag != 'null':
			num = int(input('输入数量'))	
			nowTotal = int(list(flag.values())[0])*num;
			if money > nowTotal:
				money = money - nowTotal;
				total = total+ nowTotal;
				goods_list[list(flag.keys())[0]] += num;
				print('%s*%s>>%s元添加成功'%(list(flag.keys())[0],num,nowTotal))
				print('当前余额%s'%money)
			else:
				print('资金不够')
				print('当前余额%s'%money)
