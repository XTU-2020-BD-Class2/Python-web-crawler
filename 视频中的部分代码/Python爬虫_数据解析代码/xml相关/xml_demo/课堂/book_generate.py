import requests
import os
import xml.etree.ElementTree as ET
from io import StringIO
# 0. 各种配置变量
key = "5f63b9602b5b0fb228aaa3963c5f9e84"
book_catalog_url = "http://apis.juhe.cn/goodbook/catalog?key={}&dtype=xml".format(key)
catalog_cache_file_path = "cache/catalog.xml"

# 1. 结合缓存机制, 来请求所有的图书分类数据
if not os.path.exists(catalog_cache_file_path):
    print("网络加载")
    book_catalog_resp = requests.get(book_catalog_url)
    with open(catalog_cache_file_path, "w", encoding="utf-8") as f:
        f.write(book_catalog_resp.text)

# xml
book_catalog_et = ET.parse(catalog_cache_file_path)
# print(book_catalog_et)
# 状态码是否是200
result_code = book_catalog_et.find("resultcode").text
# print(result_code)
if result_code != "200":
    print("当前目录加载失败, 直接退出!")
    exit(200)

catalogs = book_catalog_et.find("result").findall("item")
for catalog in catalogs:
    # print(catalog)
    id_str = catalog.find("id").text
    catalog_str = catalog.find("catalog").text
    print(id_str, catalog_str)

# 2. 给我一个分类的id< 发送一个网络请求->图书详情列表
cata_id = input("请输入你要浏览的分类ID:")
book_detail_url = "http://apis.juhe.cn/goodbook/query?key={}&catalog_id={}&pn=1&rn=15&dtype=xml".format(key, cata_id)
# print(book_detail_url)
book_detal_resp = requests.get(book_detail_url)
book_detail_et = ET.parse(StringIO(book_detal_resp.text))
print(book_detail_et)
book_items = book_detail_et.find("result").find("data").findall("item")

keys = ["title", "img", "sub1", "catalog", "tags", "bytime", "sub2"]

book_dir_temp = """
    <div class="box">
        <a href="{}">
            <img src="{}" alt="">
            <h4>{}</h4>
        </a>
    </div>
"""
book_dir_result = ""
for book_item in book_items:
    # print(book_item)
    title = book_item.find("title").text
    # 1. 读取模板文件内容(字符串) 2. 替换好之后, 写入到一个新的文件
    with open("book_temp/book_detail_temp.html", "r", encoding="utf-8") as book_detail_temp_file, open("book_generate_dir/{}.html".format(title), "w", encoding="utf-8") as book_detail_file:
        book_detail_temp_str = book_detail_temp_file.read()
        for key in keys:
            book_detail_temp_str = book_detail_temp_str.replace("{{" + key + "}}", book_item.find(key).text)

        book_detail_file.write(book_detail_temp_str)

    img_url =  book_item.find("img").text
    book_dir_result += book_dir_temp.format("{}.html".format(title), img_url, title)

with open("book_temp/mulu_temp.html", "r", encoding="utf-8") as temp:
    result = temp.read().replace("{{content_list}}", book_dir_result)
    with open("book_generate_dir/index.html", "w", encoding="utf-8") as f:
        f.write(result)
