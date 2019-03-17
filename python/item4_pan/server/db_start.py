import os
import sys

path = os.path.dirname(__file__)
sys.path.append(path)

from core import db

if __name__ == '__main__':
    print('数据库开启。。。。。。。')
    db.run()

