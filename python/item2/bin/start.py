'''
 1 这是一个信用卡管理程序
    2 用户手持信用卡购物，使用函数，按照软件开发规范
    3 用户名密码存放于文件中，支持多用户登陆，使用json
    4 程序启动，先登录或者注册，保存信息到文件中，记录日志
    5 用户的登陆，密码输错三次，锁定，不能再登录
    6 用户可以取现，消费，还款，提额
    7 允许用户根据商品编号购买商品，用户选择商品，检测余额，够用扣款，不够用提示，用户行为都要记录日志
    8 用户可以随时退出，退出时，打印已购买商品和余额
'''
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from python.item2.core import src

if __name__ == '__main__':
    src.run()