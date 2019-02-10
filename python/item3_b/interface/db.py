from python.item3_b.conf import setting

import pickle, os


def save(status, obj, name):
    path = setting.DB_PATH + '/' + status + '/' + name
    print(path)
    with open(path, 'wb+') as f:
        pickle.dump(obj, f)


def get_info(status, name):
    path = setting.DB_PATH + '/' + status + '/' + name

    with open(path, 'rb') as f:
        return pickle.load(f)


def get_list(status):
    path = setting.DB_PATH + '/' + status
    return os.listdir(path)


if __name__ == '__main__':
    # obj = {'username': 'name'}
    save('school', ['AI','Python'], '上海')
    arr = get_info('school', '上海')
    arr.append('dasd')
    print(arr)
    #print(get_list('school'))
