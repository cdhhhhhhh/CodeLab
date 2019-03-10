import json
import time
from python.item4_qq.server.lib import lib
from python.item4_qq.server.conf.conf import *

print('服务器开启。。。。。。。')


def run():
    while True:
        localtime = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

        server_data, server_addr = server.recvfrom(1024)
        server_data_json = json.loads(str(server_data, encoding="utf8"))

        if server_data_json['type'] == 'check_name':
            if not lib.check_name(server_data_json['msg']['name']):
                server.sendto('存在用户名'.encode('utf-8'), server_addr)
            else:
                server.sendto('不存在用户名'.encode('utf-8'), server_addr)

        if server_data_json['type'] == 'register':
            lib.register(server_data_json['msg'])
            server.sendto('注册成功'.encode('utf-8'), server_addr)

        if server_data_json['type'] == 'login':
            if lib.login(server_data_json['msg']):

                user_list[server_data_json['msg']['name']] = server_addr

                server.sendto('登录成功'.encode('utf-8'), server_addr)
            else:
                server.sendto('登录失败'.encode('utf-8'), server_addr)
        if server_data_json['type'] == 'user_list':
            server.sendto(bytes(json.dumps(user_list), encoding='utf-8'), server_addr)

        if server_data_json['type'] == 'check_person_msg':
            server.sendto(bytes(json.dumps(
                msg_person_queue[server_data_json['msg']['current_username']][server_data_json['msg']['chat_target']]),
                encoding='utf-8'), server_addr)

        if server_data_json['type'] == 'send_person_msg':
            #初始化队列
            if server_data_json['msg']['chat_target'] not in msg_person_queue.keys():
                msg_person_queue[server_data_json['msg']['chat_target']] = {}
            if server_data_json['msg']['current_username'] not in msg_person_queue[
                server_data_json['msg']['chat_target']].keys():
                msg_person_queue[server_data_json['msg']['chat_target']][
                    server_data_json['msg']['current_username']] = {}
            #推送队列
            msg_person_queue[server_data_json['msg']['chat_target']][server_data_json['msg']['current_username']][
                localtime] = \
                server_data_json['msg']['msg']
            server.sendto('发送成功'.encode('utf-8'), server_addr)
            print(msg_person_queue)

        if server_data_json['type'] == 'check_chatroom_msg':
            server.sendto(bytes(json.dumps(msg_chatroom_queue), encoding='utf-8'), server_addr)
        if server_data_json['type'] == 'send_chatroom_msg':
            msg_chatroom_queue.append(
                [localtime, server_data_json['msg']['current_username'], server_data_json['msg']['msg']])
            server.sendto('发送成功'.encode('utf-8'), server_addr)
