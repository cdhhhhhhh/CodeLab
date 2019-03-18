# encoding: utf-8
import socket
import struct
import json
import os
import hashlib

s = socket.socket()
s.bind(("127.0.0.1", 8081))  # 绑定
s.listen(5)  # 监听

conn, addr = s.accept()
head_msg = json.loads(str(conn.recv(3024), encoding='utf-8'))
print(head_msg)
with open('./text.md', 'wb') as f:
    current_size = 0
    upload_speed = 2048
    while current_size < int(head_msg['file_size']):
        current_size = current_size + upload_speed
        f.write(conn.recv(upload_speed))

with open('./text.md', 'rb') as f:
    md5 = hashlib.md5()
    md5.update(f.read())
    md5 = md5.hexdigest()
    print(md5)
