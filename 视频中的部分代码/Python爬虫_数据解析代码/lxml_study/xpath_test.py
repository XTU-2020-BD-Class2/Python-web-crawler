from lxml import etree


et = etree.parse("test.xml")

# print(et.xpath("/person//color"))
# print(et.xpath("//color/."))

# print(et.xpath("//dog/../name/text()"))
# print(et.xpath("//dog/preceding-sibling::name/text()"))
# print(et.xpath("//dog/following-sibling::name/text()"))

# print(et.xpath("//dog/@type"))
# print(et.xpath("//dog//text()"))
# print(et.xpath("//dog/node()"))

# print(et.xpath("//pet/*[last()-1]/name/text()"))
# print(et.xpath("//pet/*[position() > 1]/name/text()"))
# print(et.xpath("//pet/*[age>=2]/name/text()"))

# print(et.xpath("//pet//age[text()>=2]/text()"))
# print(et.xpath("//pet//age[text()>=2]/.."))
# print(et.xpath("//pet/*[@master='sz']/name/text()"))
# print(et.xpath("//pet/*[contains(@master, 'sz')]/name/text()"))

# print(et.xpath("//dog"))
# print(et.xpath("//cat"))

# print(et.xpath("//dog | //cat"))

# cat = et.xpath("//cat")[0]
# print([cat, cat, cat])

# print(et.xpath("//pet/*[@master='sz'] | //cat"))


# print(et.xpath("//name/text()"))
# print(et.xpath("//dog")[0].xpath("/name/text()"))
# print(et.xpath("//dog")[0].xpath("/person"))
# print(et.xpath("//dog")[0].xpath(".//name/text()"))

with open("伪元素.html", "r", encoding="utf-8") as f:
    et2 = etree.HTML(f.read())
    print(et2.cssselect("a:after"))
