from lxml import etree
# from lxml import html
# html.fromstring()

et = etree.parse("test.xml")

# age = et.find("age")
color = et.find("dog").find("color")
new_ele = etree.fromstring("<new>new</new>")
# age.addnext(new_ele)
# age.addprevious(new_ele)

# age.getparent().remove(age)
# print(et.getelementpath(color))
# print(et.getpath(color))

# with open("new.xml", "w", encoding="utf-8") as f:
et.write("new.xml", encoding="utf-8")