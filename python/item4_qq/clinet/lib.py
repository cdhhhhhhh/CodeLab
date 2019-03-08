import socket
from python.item4_qq.clinet import chat
import json

current_username = ''


def register():
    name = input('请输入用户名')
    state = send_msg('check_name', {'name': name})
    if state == '存在用户名':
        print('存在用户名')
        return
    password = input('请输入密码')
    send_msg('register', {name: password})
    print('注册成功')


def login():
    global current_username
    name = input('请输入用户名')
    state = send_msg('check_name', {'name': name})
    if state == '不存在用户名':
        print('不存在用户名')
        return
    password = input('请输入密码')
    if send_msg('login', {'name': name, 'password': password}) == '登录成功':
        current_username = name
        chat.run()
    print('登录失败')
    return


def chat_person():
    user_list = send_msg('user_list', '')
    print(user_list)
    chat_target = input('输入聊天用户名')
    while True:
        msg = input('输入发送内容 q退出 l刷新回复内容')
        if msg == 'q':
            return
        elif msg == 'l':
            check_msg = json.loads(
                send_msg('check_person_msg', {'current_username': current_username, 'chat_target': chat_target}))
            for k in check_msg:
                print(k + ' ' + check_msg[k])
        else:
            send_msg('send_person_msg', {'current_username': current_username, 'chat_target': chat_target, 'msg': msg})


def chat_room():
    while True:
        msg = input('输入发送内容 q退出 l刷新当前聊天室内容')
        if msg == 'q':
            return
        elif msg == 'l':
            for i in json.loads(send_msg('check_chatroom_msg', ''),
                                ):
                print(i[0] + '用户名' + i[1] + ' 消息：' + i[2])
        else:
            send_msg('send_chatroom_msg', {'current_username': current_username, 'msg': msg})


def send_msg(ty, msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = bytes(json.dumps({'type': ty, 'msg': msg}), encoding='utf-8')
    client.sendto(msg, ('127.0.0.1', 8083))
    res, server_addr = client.recvfrom(1024)
    return str(res, encoding='utf-8')
