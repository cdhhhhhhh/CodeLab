import socket
import os

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8083))
phone.listen(5)
print('start..')
while True:
    conn, client_address = phone.accept()
    while True:
        try:
            print('连接：', conn, client_address)
            msg = conn.recv(1024)
            command_info = os.popen(bytes.decode(msg))
            for i in command_info:
                print('客户端：', i)
                conn.send(str.encode(i))
        except Exception:
            break

    conn.close()
phone.close()
