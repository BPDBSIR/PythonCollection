import requests
from bs4 import BeautifulSoup
import threading

"""
wallhaven.cc
"""


def requestWallHaven(page, root_dir):
    """
    壁纸数据爬取
    :param page: 页数
    :param root_dir: 图片存放地址
    :return:
    """
    print("当前线程 => %s " % threading.current_thread().name)
    res = requests.get("https://wallhaven.cc/hot?page=" + page).text
    soup = BeautifulSoup(res, "html.parser")
    for item in soup.find_all("a", "preview"):
        print("页面地址: %s" % item.get("href"))
        body = requests.get(item.get("href")).text
        body_soup = BeautifulSoup(body, "html.parser")
        img_url = body_soup.find("img", id="wallpaper").get("src")
        print("图片地址: %s" % img_url)
        data = img_url.split("/")
        file_name = data[len(data) - 1]
        print("文件名称: %s " % file_name)
        with open(root_dir + file_name, "wb") as f:
            f.write(requests.get(img_url).content)

    print("Page => %s  Success！" % page)


if __name__ == '__main__':
    # Current-Page 32
    for i in range(19, 130):
        t = threading.Thread(target=requestWallHaven, name="Thread" + str(i), args=(str(i), "F:\\Wallhaven\\"))
        t.start()
        t.join()
    print("全部下载完毕！")
