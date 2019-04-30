from multiprocessing import Process
import requests
import re


def get_list(url):
    r = requests.get(url)
    reg_article = '<div class="post_item_body">[\D\d]*</div>'
    reg_link = 'https://www\.cnblogs\.com/du-hong/p/[\d]*\.html'
    article = re.findall(reg_article, r.text, flags=0)
    article_list = [re.search(reg_link, i) for i in article if
                    re.search('python', i, flags=re.I)]


def ws_link():
    list = []
    with open('./linklist','r') as fs:
        list = fs.read()

page_list = []
if __name__ == '__main__':
    p = Process(target=get_list,args=page_list)
