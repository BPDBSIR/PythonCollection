import requests
from bs4 import BeautifulSoup
import re

base_url = "http://www.1ppt.com"
root_dir = "F:\\第一PPT\\简洁\\"


def requestDetail():
    res = requests.get(base_url + "/moban/jianjie/")
    res.encoding = "GB2312"
    soup = BeautifulSoup(res.text, 'html.parser')
    i = 0
    result = set()
    for item in soup.find_all("a", href=re.compile("/article")):
        result.add(base_url + item["href"])
    for iss in result:
        con = requests.get(iss)
        con.encoding = "GB2312"
        con_soup = BeautifulSoup(con.text, "html.parser")
        title_div = con_soup.find("div", "ppt_info clearfix")
        title = title_div.contents[1].string
        down_ul = con_soup.find("ul", "downurllist")
        down_url = base_url + down_ul.contents[1].contents[0]["href"]
        file_soup = BeautifulSoup(requests.get(down_url).text, "html.parser")
        file_url = file_soup.find("li", "c1").contents[0]["href"]
        print("名称 => %s 介绍地址 => %s 下载链接 => %s " % (title, down_url, file_url))
        with open(root_dir + title + ".zip", "wb") as f:
            f.write(requests.get(file_url).content)


def requestCategory():
    cate = requests.get(base_url)
    cate.encoding = "GB2312"
    cate_soup = BeautifulSoup(cate.text, "html.parser")
    dd = cate_soup.find_all("a", href=re.compile(r'^/moban'))
    for n in dd:
        print(n)
    # cate_ul = cate_soup.find("div", "col_nav i_nav clearfix")
    # for item in cate_ul:
    #     print(type(item))


requestCategory()
