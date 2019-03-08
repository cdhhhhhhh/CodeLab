import json


def db_handle(rw, info=None):
    path = '/Users/cuidaohan/item/lab/python/item4_qq/server/db'
    if rw == 'r':
        with open(path, 'r') as f:
            return json.loads(f.read())
    elif rw == 'w':
        with open(path, 'w') as f:
            f.write(json.dumps(info))
            f.flush()


def check_name(name):
    list_name = db_handle('r').keys()
    if name in list_name:
        return False
    else:
        return True


def register(info):
    update_list = db_handle('r')
    update_list.update(info)
    db_handle('w', update_list)


def login(info):
    user_list = db_handle('r')
    if (info['name'] in user_list) and (user_list[info['name']] == info['password']):
        return True
    else:
        return False

if __name__ == '__main__':
    # db_handle('w', {'test': '123'})
    register({'test': '123'})
    register({'test3': '123'})
    print(db_handle('r'))
    pass
