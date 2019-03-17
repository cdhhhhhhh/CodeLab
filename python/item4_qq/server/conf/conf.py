import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8083))
user_list = {}
msg_person_queue = {}
msg_chatroom_queue = []
