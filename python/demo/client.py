# encoding: utf-8
import socket
import os
import hashlib
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建
s.connect(("127.0.0.1", 8081))  # 连接

print(s.recvfrom(1020))