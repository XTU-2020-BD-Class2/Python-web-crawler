import xml.etree.ElementTree as ET

# ------------------节点创建----------------------
# ele = ET.Element("sz", {"a": "aa", "b": "bb"})

# ------------------节点转节点树-》保存到文件----------------------
# ele = ET.Element("sz", {"a": "aa", "b": "bb"})
# ele.text = "xxx"
# et = ET.ElementTree(ele)
# et.write("ele.xml", encoding="utf-8")

# ------------------节点各个属性----------------------
# et = ET.ElementTree(file="ele.xml")
# name_ele = et.find("name")
# print(name_ele)
# print(name_ele.tag) # name
# print(name_ele.attrib) # {"a": "aa"}
# print(name_ele.text) # xxx
# print(name_ele.tail) # tail_content

# ------------------节点的属性操作----------------------
# print(ele.keys())
# print(ele.items())
# for key, value in ele.items():
#     print(key, value)
# print(ele.get("c", default="cc"))
# print(ele.attrib["b"])
# ele.set("c", "3336")

# ------------------节点的节点操作-增加----------------------
# sub_ele = ET.Element("name")
# sub_ele.text = "888"
# ele.append(sub_ele)
# sub_ele2 = ET.Element("addr")
# sub_ele2.text = "上海"
# # ele.append(sub_ele2)
# ele.insert(0, sub_ele2)

# et = ET.ElementTree(file="ele.xml")
# root = et.getroot()
# print(root[0])

# et = ET.ElementTree(file="ele.xml")
# root = et.getroot()
# # sub_ele = ET.Element("name")
# # sub_ele.text = "888"
# # root.append()
# sub_ele = ET.SubElement(root, "pet", {"age": "2"})
# print(sub_ele)
# et.write(file_or_filename="ele.xml", encoding="utf-8")

# ------------------节点的节点操作-删除----------------------
# et = ET.ElementTree(file="ele.xml")
# root = et.getroot()
# pet = et.find("pet")
# root.remove(pet)
#
# et.write(file_or_filename="ele.xml", encoding="utf-8")


# ------------------节点的节点操作-查询----------------------
# et = ET.ElementTree(file="ele.xml")
# ele = et.getroot()
# # print(list(ele))
# result = ele.itertext()
# for text in result:
#     print(text)
# print(result)
# et.write(file_or_filename="ele.xml", encoding="utf-8")

# ------------------节点的节点操作-清空自己----------------------
# et = ET.ElementTree(file="ele.xml")
# ele = et.find("addr")
# ele.clear()
# print(ele)
# print(ele.tag)
# print(ele.text)
# print(ele.attrib)
# print(ele.tail)
# print(list(ele))
# et.write(file_or_filename="ele.xml", encoding="utf-8")

# ------------------节点的节点操作-扩展兄弟节点----------------------
# et = ET.ElementTree(file="ele.xml")
# print(et.getroot())
# ele = et.find("name")


# et.write(file_or_filename="ele.xml", encoding="utf-8")


et = ET.iterparse("ele.xml", events=("start", "end"))
print(et)
for evt,ele in et:
    if evt == "end":
        print(ele.text)
        print(ele.tag)