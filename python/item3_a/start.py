import sys
import os

path = os.path.dirname(__file__)
sys.path.append(path)
from python.item3.core import src

if __name__ == '__main__':
    src.run()
