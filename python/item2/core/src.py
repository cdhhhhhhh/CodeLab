from python.item2.conf import settings
from python.item2.lib import common
import time

logger=common.get_logger(__name__)

current_user={'user':None,'login_time':None,'timeout':int(settings.LOGIN_TIMEOUT)}

count = 0
goods={'mac': 100, 'apple': 10}
current_goods={'mac': 0, 'apple': 0}
user = common.conn_db()
def auth(func):
    def wrapper(*args,**kwargs):
        while True:
            global count
            if count == 3:
                logger.error('登入次数上限')
                exit()
            if current_user['user']:
                interval = time.time() - current_user['login_time']
                if interval < current_user['timeout']:
                    return func(*args, **kwargs)
            name = input('name>>: ')
            password = input('password>>: ')
            if user.get(name):
                if password == user.get(name).get('password'):
                    logger.info('登录成功')
                    current_user['user'] = name
                    current_user['login_time'] = time.time()
                    return func(*args, **kwargs)
                else:
                    logger.error('密码错误')
                    count+=1
            else:
                logger.error('用户名不存在')
                time.sleep(0.1)
                count = 0
    return wrapper


def buy():

    for k,v in goods.items():
        print('商品%s价格%s'%(k,v))
    print('返回上一级?q')
    while True:
        key = input('输入商品')
        if key =='q':
            return
        if key in goods:
            count = input('输入数量')
            if common.consume_goods(user,current_user['user'],int(count)*goods[key]):
                logger.info('购买成功')
                current_goods[key]+=int(count)


def check_money():
    logger.info('余额%s'%user[current_user['user']]['money'])
def draw_money():
    money = input('输入取出金额')
    common.consume_goods(user, current_user['user'], int(money))
    logger.info('余额%s'%user[current_user['user']]['money'])


def add_limit():
    money = input('输入提额金钱')
    common.add_limit(user, current_user['user'], int(money))
    logger.info('额度%s'%user[current_user['user']]['limit'])

def return_money():
    money = input('输入取出还钱金钱')
    if money <= user[current_user['user']]['limit']:
        common.add_money(user, current_user['user'], int(money))
    else:
        print('金额大于还款金额')




@auth
def run():
    global user
    print('''
1.购物
2.查看余额
3.还款
4.提额
5.取钱
6.退出
    ''')
    while True:
        choice = input('>>: ').strip()
        if not choice:continue
        if choice == '1':
            buy()
        if choice == '2':
            check_money()
        if choice == '3':
            return_money()
        if choice == '4':
            add_limit()
        if choice == '5':
            draw_money()
        if choice == '6':
            common.fs_db(user)
            exit()

