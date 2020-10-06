import requests
import os

# 1. 目录加载
# 判定目录缓存文件是否存在？
category_file_path = "category.xml"
if not os.path.exists(category_file_path):
    url = "http://apis.juhe.cn/goodbook/catalog?key=5f63b9602b5b0fb228aaa3963c5f9e84&dtype=xml"
    resp = requests.get(url)
    xml_str = resp.text
    with open(category_file_path, "w", encoding="utf-8") as f:
        f.write(xml_str)

from xml.etree.ElementTree import *
et = ElementTree(file=category_file_path)
items = et.find("result").findall("item")
# print(items)
for item in items:
    id_ = item.find("id").text
    category = item.find("catalog").text
    print(id_, category)

num = input("请选择目录编号：")
detail_url = "http://apis.juhe.cn/goodbook/query?key=5f63b9602b5b0fb228aaa3963c5f9e84&catalog_id={}&pn=1&rn=10&dtype=xml".format(num)
detail_resp = requests.get(detail_url)
detail_xml_str = detail_resp.text

from io import StringIO
detail_et = ElementTree(file=StringIO(detail_xml_str))
books = detail_et.find("result").find("data").findall("item")

# 生成详情和目录html文件
index_str = ""
index_temp = """
    <div class="box">
        <a href="{}">
            <img src="{}" alt="">
            <h4>{}</h4>
        </a>
    </div>
"""
keys = {"title", "img", "sub1", "catalog", "tags", "bytime", "sub2"}
for book in books:

    # print(title, sub, img)
    title = book.find("title").text
    with open("book_temp/detail.html", "r", encoding="utf-8") as f1, open("book_temp/" + title + ".html", "w", encoding="utf-8") as f2:
        templete = f1.read()
        for key in keys:
            templete = templete.replace("{{" + key + "}}", book.find(key).text)
        f2.write(templete)

    # index_str 拼接
    img = book.find("img").text
    sub1 = book.find("sub1").text
    index = index_temp.format(title + ".html", img, title)
    index_str += index

with open("book_temp/index.html", "r", encoding="utf-8") as index_tmp_file, open("book_temp/mulu.html", "w", encoding="utf-8") as mulu_file:
    index_tmp = index_tmp_file.read().replace("{{content_list}}", index_str)
    mulu_file.write(index_tmp)