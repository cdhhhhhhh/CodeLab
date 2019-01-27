from python.item2.conf import settings
import logging
import logging.config
import json

def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(name)  # 生成一个log实例
    return logger


def conn_db():
    db_path=settings.DB_PATH
    dic=json.load(open(db_path,'r',encoding='utf-8'))
    return dic

def fs_db(info):
    db_path=settings.DB_PATH
    with open(db_path,'w',encoding='utf-8') as fs:
        fs.write(json.dumps(info))
def consume_goods(userlist,username,price):
    if price<userlist[username]['money']:
        userlist[username]['money']-= price
        return True
    else:
        print('余额不足')
        return False
def add_money(userlist,username,money):
        userlist[username]['money']+= money

def add_limit(userlist,username,limit):
    userlist[username]['limit'] += limit
