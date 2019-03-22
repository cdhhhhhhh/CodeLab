# encoding: utf-8
import socket
import struct
import json
import os
import hashlib


def creat():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8089))  # 绑定
    s.listen(5)  # 监听

    return s


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s


server = creat()
conn, addr = server.accept()
print(type(eval(str(conn.recv(5222),encoding='utf-8'))))