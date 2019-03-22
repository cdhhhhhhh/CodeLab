import os
import sys

path = os.path.dirname(__file__)
sys.path.append(path)

from core import main

if __name__ == '__main__':
    print('服务器开启。。。。。。。')
    main.run()
