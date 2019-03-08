import socket
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8081))

while True:
    info = input('input command')
    phone.send(info.encode('utf-8'))

    recv_size = struct.unpack("i", phone.recv(4))[0]
    print(recv_size)

    data = phone.recv(4)
    curr_size = 0
    while curr_size < recv_size:
        data = phone.recv(512)
        print(data.decode('utf-8'))
        curr_size = curr_size + 512

phone.close()
