from pyquery import PyQuery as PQ
from lxml import etree

# 2. 节点操作

with open("test.xml", "r", encoding="utf-8") as f:
    pq = PQ(f.read())
    # print(pq("*[master='sz']"))
    # print(pq.find("*[master='sz']"))
    # print(pq.find("name"))
    # print(pq.children("name"))
    # print(type(pq("name")))

    # print(pq("cat>age").parent())
    # print(pq("cat>age").parents("pet"))
    # print(pq("cat>age").siblings("name2"))

    # print(pq("name"))
    # print(pq("name")[1])
    # print(type(pq("name")[1]))

    # print(pq("name").eq(1))
    # print(type(pq("name").eq(1)))

    # print(pq.items("name"))
    # print(type(pq.items("name")))
    # for ele in pq.items("name"):
    #     print(ele)
    #     print(type(ele))
    # def test(i, e):
    #     print(i, e.xpath(".//text()"))
    # pq("name").each(test)

    # pq("name").eq(0).replace_with("<a>itlike</a>")
    # pq("name").eq(0).after("""
    #     <div>
    #         <a>itlike</a>
    #     </div>
    #
    # """)
    # pq("name").eq(0).prepend("xxx")
    # print(pq)

    # print(pq("name").attr.cls)
    # print(pq("name").attr["cls"])
    # print(pq("name").attr("cls"))

    # pq("name").eq(0).attr("cls", "new_value")
    # pq("name").attr("cls", "new_value")
    # pq("name").remove_attr("cls")


    # name = pq("name").eq(0)
    # name.add_class("new")
    # # name.add_class("new2")
    # # name.remove_class("new2")
    # name.toggle_class("new2")
    # print(name.has_class("new"))
    #
    # print(pq)

    # print(pq("name").text(""))
    pq("name").empty()
    # print(type(pq("name").text()))
    print(pq)






# 1. 文档加载
# pq = PQ("<a>xxx</a>")

# ele = etree.fromstring("<a>xxx</a>")
# pq = PQ(ele)

# pq = PQ(filename="test.xml", encoding="utf-8")
# with open("test.xml", encoding="utf-8") as f:
#     pq = PQ(f.read())
    # print(pq)
# pq = PQ(url="http://v.juhe.cn/postcode/query?postcode=215001&dtype=xml&key=5741eee83b57d8c5eaee729a3606f72b")
#
# print(pq)


