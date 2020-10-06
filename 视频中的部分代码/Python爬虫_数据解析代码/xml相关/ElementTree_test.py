import xml.etree.ElementTree as ET


et = ET.ElementTree(file="test.xml")
# print(et)
# print("根节点", et.getroot())
# print(et.find("name"))
# print(et.find("itlike:student", namespaces={"itlike": "http://www.itlike.com/itlike"}).attrib)
# print(et.find("{http://www.itlike.com/itlike}student").attrib)

# print(et.findall("student"))
# print(et.findtext("studentxx", default="123"))



# 迭代器
# eti = et.iter(tag="name")
# # print(eti)
# for ele in eti:
#     print(ele)

#
# eti = et.iterfind("name")
# for ele in eti:
#     print(ele)
#     print("-" * 30)

et.write("new_test.xml", encoding="utf-8")
