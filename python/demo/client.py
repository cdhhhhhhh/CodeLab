# encoding: utf-8
import socket
import os
import hashlib
import json

s = socket.socket()  # 创建
s.connect(("127.0.0.1", 8081))  # 连接

file_text = ''
file_info = {}
with open('/Users/cuidaohan/Desktop/N-blog/README.md', 'rb') as f:
    file_text = f.read()
file_info['file_name'] = 'test_name'
file_info['file_size'] = os.path.getsize('/Users/cuidaohan/Desktop/N-blog/README.md')

md5 = hashlib.md5()
md5.update(file_text)
md5 = md5.hexdigest()
file_info['md5'] = md5

s.send(bytes(json.dumps(file_info), encoding='utf-8'))

with open('/Users/cuidaohan/Desktop/N-blog/README.md', 'rb') as f:
    current_size = 0
    upload_speed = 2048
    while current_size < int(file_info['file_size']):
        current_size = current_size + upload_speed

        s.send(f.read(upload_speed))


s.close()