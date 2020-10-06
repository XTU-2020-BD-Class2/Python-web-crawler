from bs4 import BeautifulSoup, SoupStrainer

content_str = """
    <person>
        <name>sz</name>
        <pet>
            <dog master="sz">
                <name>煤球</name>
                <age>2</age>
                <color>五彩斑斓黑</color>
            </dog>
            <cat master="sz">
                <name>皮皮</name>
                <age>0.2</age>
                <color>黑白条纹</color>
            </cat>
        </pet>
    </person>
"""

soup_strainer = SoupStrainer("cat")

soup = BeautifulSoup(content_str, features="lxml", parse_only=soup_strainer)

# 解析部分文档
print(soup)





exit(0)
# 节点导航

color = soup.find("color")
print(color)

import copy
new_color = copy.copy(color)
# print(id(color), id(new_color))
# print(color, new_color)
new_color.name = "xxx"
pet = soup.pet
pet.append(new_color)
#
print(soup)


# print(color.find_parents("pet"))





exit(0)
# name = soup.find("name")
# print(name.find_all_next(text="sz"))
# print(name.find_all_next("name"))


sz = soup.find(text="sz")
# print(sz.find_all_next("sz"))

name = soup.find("name")
# print(name.find_next_siblings("dog"))
# print(name.find_all_next("person"))

# print(name.find_all_previous("person"))
# print(name.find_previous_siblings("person"))


print(name.next_siblings)

for ele in name.next_siblings:
    print(ele)





exit(0)
# 新增节点
d_age = soup.find("d_age")

new1 = soup.new_tag("new1")
new2 = soup.new_tag("new2")

# d_age.insert_before(new1, new2)
# d_age.insert_after(new1, new2)


# d_age.append(new1)
# d_age.extend([new1, new2])
d_age.insert(0, new1)

print(soup)


exit(0)
# 提取节点
d_age = soup.d_age
print(d_age.extract())

print(soup)


exit(0)
# 包装和解包

# meiqiu = soup.find(text="煤球")
name = soup.find("name")

# meiqiu.wrap(name)


name.unwrap()
print(soup)
print(name)








exit(0)
# 替换节点
# name = soup.find("name")
sz = soup.find(text="sz")
d_age = soup.d_age

new_tag = soup.new_tag("xxx")

# print(name, d_age)
new_content = soup.new_string("new_content")
sz.replace_with(new_content)

print(soup)



# setup TODO
# d_name = soup.d_name
# person = soup.person
# # print(d_name, person)
# d_name.setup(parent=person)
# print(d_name.parent)
#
# print(soup)