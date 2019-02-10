from python.item3_b.conf import setting

import pickle, os
from python.item3_b.interface import common



def save(status, obj, name):
    path = setting.DB_PATH + '/' + status + '/' + name
    print(path)
    with open(path, 'wb+') as f:
        pickle.dump(obj, f)
        common.get_logger(__name__).info('存储成功')


def get_info(status, name):
    path = setting.DB_PATH + '/' + status + '/' + name

    with open(path, 'rb') as f:
        common.get_logger(__name__).info('读取信息')
        return pickle.load(f)


def get_list(status):
    path = setting.DB_PATH + '/' + status
    common.get_logger(__name__).info('读取列表')
    return os.listdir(path)


if __name__ == '__main__':
    # obj = {'username': 'name'}
    # save('school', ['AI','Python'], '上海')
    # arr = get_info('school', '上海')
    # arr.append('dasd')
    # print(arr)
    pass
