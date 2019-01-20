menu = {
	'北京':{
		'海淀':{
			'五道口':{
				'soho':{},
				'网易':{},
				'google':{}
			},
			'中关村':{
				'爱奇艺':{},
				'汽车之家':{},
				'youku':{},
			},
			'上地':{
				'百度':{},
			},
		},
		'昌平':{
			'沙河':{
				'电子厂':{},
				'北航':{},
			},
			'天通苑':{},
			'回龙观':{},
		},
		'朝阳':{},
		'东城':{},
	},
	'上海':{
		'闵行':{
			"人民广场":{
				'炸鸡店':{}
			}
		},
		'闸北':{
			'火车战':{
				'携程':{}
			}
		},
		'浦东':{},
	},
	'山东':{},
}
layer = 0


for key,value in menu.items():
	print('%s%s'%(key,value))
	
def go_layer():
	
	temp_key = list(menu.keys())
	temp_values = list(menu.values())
	tempK = []
	tempV =[]
	for i in range(0,layer):
		for item in temp_values:
			tempV.extend(item.values())
			tempK.extend(item.keys())
		temp_key =tempK
		temp_values = tempV
		tempV = []
		tempK =[]
	for i in range(0,len(temp_values)):
		print('%s%s'%(temp_key[i],temp_values[i]))
	return;

while True:
	flag = input('g前进一层,b后退一层,q退出程序?')
	if flag == 'g'and layer<=3:
		layer=layer+1
		go_layer()
	if flag == 'b'and layer>=0:
		layer=layer-1
		go_layer()
	if flag == 'q':
		exit()
	if layer>3 or layer<0:
		print('暂无信息')
	
		
