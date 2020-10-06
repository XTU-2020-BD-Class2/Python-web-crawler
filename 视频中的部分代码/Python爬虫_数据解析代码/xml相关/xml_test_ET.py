import xml.etree.ElementTree as ET

# with open("test.xml", "r", encoding="utf-8") as f:
#     # result = ET.parse("test.xml")
#     result = ET.parse(f)
#     print(result)

# xml 字符串
xml_str = """
    <name>sz</name>
"""

# from io import StringIO
# file = StringIO(xml_str)
# result = ET.parse(file)
# print(result)


# 通过一个xml文档或者字符串 -》 Element
# ET.fromstring
# with open("test.xml", "r", encoding="utf-8") as f:
#     result = ET.XML(f.read())
#     print(result)

result = ET.fromstringlist(("<person><name>sz</name>", "<age>18</age></person>"))
print(result)




# ElementTree 类
# et = ET.ElementTree(result)
et = ET.ElementTree(file="test.xml")
print(et)
