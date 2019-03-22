import socket
import json
from conf import setting
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((setting.server_ip, setting.server_port))


def send_msg(msg):
    msg = bytes(json.dumps(msg), encoding="utf-8")
    client.send(msg)


def recv_msg():
    res = client.recv(2048)
    return json.loads(str(res, encoding="utf-8"))


def send_file(msg):
    client.send(msg)


def recv_file(size):
    return client.recv(size)


def check_file_list(username):
    send_msg({"type": "check_list", "msg": {"username": username}})
    recv = recv_msg()
    for i in recv["msg"]["file"]:
        print("文件名==>>" + i["file_name"] + "-----------" + str(i["file_size"]) + "b")


def register(username, password):
    msg = {
        "type": "register",
        "msg": {
            "username": username,
            "password": password
        }
    }
    send_msg(msg)


def login(username, password):
    msg = {
        "type": "login",
        "msg": {
            "username": username,
            "password": password
        }
    }
    return send_msg(msg)


def login_auth(user):
    def auth(func):
        def wrapper(*args, **kwargs):
            if user["username"] == "":
                print("请注册")
            else:
                func(*args, **kwargs)

        return wrapper

    return auth


if __name__ == "__main__":
    send_msg({"type": "test"})
