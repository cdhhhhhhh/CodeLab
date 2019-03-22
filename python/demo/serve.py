# encoding: utf-8
import socket
import struct
import json
import os
import hashlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8089))
a = {"type": "register", "msg": {"username": "scdads", "password": "d"}}
s.send(bytes(json.dumps(a), encoding='utf-8'))
