import socket
import subprocess
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8081))
server.listen(5)
print('start....')

while True:
    conn, client_address = server.accept()
    while True:
        try:
            cmd = conn.recv(512)
            obj = subprocess.Popen(cmd.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            conn.send(struct.pack('i', len(stdout) + len(stderr)))
            conn.send(stdout)
            conn.send(stderr)


        except ConnectionResetError:
            break
    conn.close()

server.close()
