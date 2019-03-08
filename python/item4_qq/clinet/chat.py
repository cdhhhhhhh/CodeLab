from python.item4_qq.clinet import lib

def run():
    while True:
        tag = input('''
          1.好友聊天
          2.聊天室
          ''')
        if tag == '1':
            lib.chat_person()
        elif tag == '2':
            lib.chat_room()
