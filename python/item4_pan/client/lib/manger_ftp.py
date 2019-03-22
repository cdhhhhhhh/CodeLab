import hashlib
import os
from lib import common
import time


def get_md5(file_path):
    with open(file_path, 'rb') as f:
        md5 = hashlib.md5()
        md5.update(f.read())
        md5 = md5.hexdigest()
        return md5


def upload_file(username):
    file_path = input('输入文件绝对路径').replace(' ', '')
    if not os.path.exists(file_path):
        print('文件不存在')
        return
    file_info = {
        'username': username,
        'file_name': os.path.basename(file_path),
        'file_size': os.path.getsize(file_path),
        'md5': get_md5(file_path)
    }
    recv_data = common.send_msg({'type': 'upload_file', 'msg': file_info})
    upload_speed = int(recv_data['msg']['speed'])
    file_info['speed'] = upload_speed
    print(recv_data)
    if recv_data['msg']['has_vip'] == '1':
        print('正在启动会员加速中')
    else:
        print('建议使用会员加速，能够更快的上传和下载')
    if recv_data['msg']['has_file'] != '1':
        common.send_msg({'type': 'upload_file', 'msg': file_info}, tuple(recv_data['msg']['db_server']))
        with open(file_path, 'rb') as f:
            current_size = 0
            while current_size < int(file_info['file_size']):
                time.sleep(1)
                print(str(current_size) + '/' + str(file_info['file_size']) + '----' + str(upload_speed) + 'b/s')
                current_size = current_size + upload_speed
                common.send_file(f.read(upload_speed), tuple(recv_data['msg']['db_server']))
                if current_size > int(file_info['file_size']):
                    time.sleep(1)
                    print('上传完成')
                    common.send_file(f.read(upload_speed - (current_size - int(file_info['file_size']))),
                                     tuple(recv_data['msg']['db_server']))
    else:
        temp = int(file_info['file_size'] / 5)
        while temp < file_info['file_size']:
            time.sleep(0.5)
            temp += temp
            print(str(temp) + '/' + str(file_info['file_size']) + '----' + str(temp) + 'b/s')
        print('上传完成')
    time.sleep(1)
    recv_data_state = common.send_msg({'type': 'upload_file_ok', 'msg': file_info})
    print(recv_data_state)


def download_file(username):
    file_name = input('输入下载文件名')
    recv_data = common.send_msg({'type': 'download_file', 'msg': {'username': username, 'file_name': file_name}})
    if recv_data['type'] == '1':
        upload_speed = recv_data['msg']['speed']
        file_size = recv_data['msg']['file_size']
        if recv_data['msg']['has_vip'] == '1':
            print('正在启动会员加速中')
        else:
            print('建议使用会员加速，能够更快的上传和下载')

        common.send_msg({'type': 'download_file', 'msg': {'username': username, 'file_name': file_name,
                                                          'file_size': file_size,
                                                          'speed': upload_speed}},
                        tuple(recv_data['msg']['db_server']))

        with open('/Users/cuidaohan/item/lab/python/item4_pan/client/db/' + file_name, 'wb') as f:
            current_size = 0
            speed_size = int(upload_speed)
            while current_size < file_size:
                print('下载数据' + str(current_size)+'/'+str(file_size)+'----'+upload_speed+'b/s')
                current_size = current_size + speed_size
                f.write(common.rev_file(speed_size))
                if current_size > file_size:
                    print('下载数据完成')
                    f.write(common.rev_file(speed_size - (current_size - file_size)))
                time.sleep(1)

    else:
        print('输入正确文件名')
