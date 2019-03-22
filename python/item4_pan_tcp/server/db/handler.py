import os
import json

db_path = '/Users/cuidaohan/item/lab/python/item4_pan_tcp/server/db/'


def mkdir(username):
    path = db_path + username
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return True
    else:
        return False


def write_user(msg):
    with open(db_path + 'user.json', 'w') as f:
        f.write(json.dumps(msg))


def read_user():
    with open(db_path + 'user.json', 'r') as f:
        return json.loads(f.read())


