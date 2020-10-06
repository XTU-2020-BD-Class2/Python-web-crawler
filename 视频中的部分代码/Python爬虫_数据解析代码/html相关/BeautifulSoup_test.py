from bs4 import BeautifulSoup

content_str = """
    <div class="box">
        <a href="1984.html">
            <h4>1984</h4>
        </a>
        <a href="1984.html">
            <h4>xxx</h4>
        </a>
    </div>
"""

soup1 = BeautifulSoup(content_str, features="lxml")

# print(soup1.find_all("a"))
# print(soup1("a"))

# print(soup1.find("a").find("h4"))
print(soup1.a.h4)


# soup2 = BeautifulSoup(content_str, features="html.parser")
# soup3 = BeautifulSoup(content_str, features="xml")
# soup4 = BeautifulSoup(content_str, features="html5lib")
# print(soup1)
# print(soup2)
# print(soup3)
# print(soup4)

# 1 美化输出
# print(soup1)
# print(soup1.prettify())

# 2 重置
# soup1.reset()
# print(type(soup1))

# 3 创建新的节点
# print(soup1.new_tag("xxx", "http://www.itlike.com", "itlike", {"age": "18"}))
# print(type(soup1.new_tag("xxx", "http://www.itlike.com", "itlike", {"age": "18"})))
#
# print(soup1.new_string("xxx"))
# print(type(soup1.new_string("xxx")))

