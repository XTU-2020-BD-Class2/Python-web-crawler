from bs4 import BeautifulSoup

with open("html_test.html", "r", encoding="utf-8") as f:
# with open("cssselector_test.xml", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, features="lxml")
    # 3. css选择器
    # print(soup.select("div#bottom img"))
    # print(soup.select_one("div#bottom img"))

    # 通配符选择器
    # print(soup.select("*"))

    # 标签选择器
    # print(soup.select("h4"))

    # 类选择器
    # print(soup.select(".box"))


    # id选择器
    # print(soup.select("xxx#top"))


    # 属性选择器
    # print(soup.select("[class~='c1']"))
    # print(soup.select(".box[hidden='1']"))
    # print(soup.select("[class='box'][hidden='1']"))


    # 关系选择器
    # print(soup.select("root>dog"))
    # print(soup.select("p>dog"))
    # print(soup.select("root name"))
    # print(soup.select("age+addr"))
    # print(soup.select("age~addr"))


    # 并且 或者
    # print(soup.select("div[hidden]"))
    # print(soup.select("xx,[hidden]"))






    # 2. 子节点查找(查找一个 或者 查找多个)
    # print(soup.find(["img", "body"], recursive=True))
    # print(soup.find(True))

    # def filter_tag(tag):
    #     # print(tag)
    #     # print("-"*30)
    #     return len(tag.name) >= 5
    # print(soup.find(filter_tag))

    # print(soup.find("div", attrs={"class": "box"}))
    # print(soup.find(attrs={"class": "box", "id": "222"}))
    # print(soup.find(text="1984").parent)
    # print(soup.find_all(id="222"))
    # print(soup.find_all(class_="box"))

    # print(soup.find_all("h4", limit=3))

    # 1. 固定的节点获取
    # div = soup("div")[1]
    # # print(div.children)
    # for div_sub in div.descendants:
    #     print(div_sub)
    #     print("---"*30)