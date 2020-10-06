from bs4 import BeautifulSoup, Tag

# Tag

content_str = """
    <person class="1班 2班" school="1中 2中">
    <name> sz </name>
    <age a_t="at">
        <a1>
            <b1>a11</b1>
        </a1>
    </age>
    <xxx/>
    </person>
"""


# soup = BeautifulSoup(content_str, features="xml")
soup = BeautifulSoup(content_str, features="lxml")

# 索引
age = soup.age
a1 = soup.a1
b1 = soup.b1

print(age.index(b1))









# 判定操作
exit(0)
# xxx = soup.xxx
# other = soup.new_tag("other")
# print(other)
# print(xxx.is_empty_element)

age = soup.age
age.clear()
print(age)






exit(0)
# 清空和删除
age = soup.age
a1 = soup.a1
age.clear(decompose=True)
# age.decompose()
print(age)
print("-"*30)
print(a1)
print("-"*30)
print(soup)





exit(0)
# 文本操作

# person = soup.person
#
# print(person.strings)
# print(person.stripped_strings)
#
# for s in person.stripped_strings:
#     print(s)



# age = soup.age
# print(age.string)
# print(type(age.string))

# age.string = "xxx"
# print(soup)

# age = soup.find("age")
# age.text = "xxx"
# print(age)

# print(person.get_text(separator="-", strip = True))
# print(person.text)
# print(type(person.text))













# 属性操作
exit(0)

person_tag = soup.person
# print(person_tag.attrs)
# print(person_tag.attrs["class"])
#
# # print(person_tag.get("school1", "222"))
# print(person_tag.get("class"))
# print(person_tag.get_attribute_list("class"))

print(person_tag.attrs["school"])

# print(person_tag.get("school1", "222"))
print(person_tag.get("school"))
print(person_tag.get_attribute_list("school"))

person_tag.attrs["addr"] = "ooo"
# del person_tag.attrs["addr"]
print(person_tag.has_attr("addr"))

# print(type(age_tag))


exit(0)
# 1. 标签名称的操作
age_tag = soup.age
print(age_tag)
print(age_tag.name)
age_tag.name = "xxx"
print(age_tag)
print(age_tag.name)