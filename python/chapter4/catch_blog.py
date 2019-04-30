from concurrent.futures import ThreadPoolExecutor
import requests
import re

data_list = [{'CategoryId': '808', 'CategoryType': 'SiteHome', 'ItemListActionName': 'PostList', 'PageIndex': str(i),
              'ParentCategoryId': '0', 'TotalPostCount': '4000'} for i in range(1, 11)]


def get_list(data):
    r = requests.post('https://www.cnblogs.com/mvc/AggSite/PostList.aspx', data=data)
    reg_article = '<a class="titlelnk"([\S\s]*?)>([\S\s]*?)</a>'
    reg_link = 'https://www\.cnblogs\.com/([\S\s]*?)/p/([\S\s]*?)\.html'
    article_list = re.findall(reg_article, r.text, flags=0)
    article_list = [re.search(reg_link, i[0]).group() for i in article_list if re.match('(Python|python)', i[1])]
    return article_list


if __name__ == '__main__':
    p = ThreadPoolExecutor()
    p_list = []
    link_list = []
    for i in range(0, 10):
        obj = p.submit(get_list, data_list[i])
        p_list.append(obj)
    for i in range(0, 10):
        link_list.append(p_list[i].result())
    with open('./linklist', 'w') as fs:
        link_list = [i for i in link_list if i != []]
        fs.write(str(link_list))
