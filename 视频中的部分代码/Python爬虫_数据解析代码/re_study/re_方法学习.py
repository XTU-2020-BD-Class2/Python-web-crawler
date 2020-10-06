import re


# 1 对正则表达式进行编译
# rc = re.compile("\d{2}")
# rc = re.compile("aa", flags=re.I)
# print(rc)
# print(type(rc))
# # rc.
# print(rc.match("Aabb"))


# 2. match
# result = re.match("(\d{4})-(0\d|1[0-2])-([0-2]\d|3[0-1])", "2018-09-27xxx")
# print(result)
# print(type(result))

# print(result.groups())
# print(result.groups()[0])
# print(result.group(1))
# print(result.group(0))

# print(result.start())
# print(result.end())
# # print(result.span())
# print(result.string)


# search
# result = re.search("(\d{4})-(0\d|1[0-2])-([0-2]\d|3[0-1])", "abcdefg2018-09-27xxx2019-09-27")
# print(result)
# print(type(result))

# findall
# result = re.findall("(\d{4})-(0\d|1[0-2])-([0-2]\d|3[0-1])", "abcdefg201a-09-27xxx201c-09-27")
# print(result)
# print(type(result))


# split
# result = re.split("(\d{4})-(0\d|1[0-2])-([0-2]\d|3[0-1])", "abcdefg2018-09-27xxx2019-09-27")
# result = re.split("-", "abcdefg2018-09-27xxx2019-09-27", maxsplit=2)
# print(result)


# sub
# result = re.sub("-","/", "abcdefg2018-09-27xxx2019-09-27", count=2)
# result = re.subn("-","/", "abcdefg2018-09-27xxx2019-09-27")
# print(result)

content = "my birthday is 2018-09-27"
print(re.match("[\w\s]*((\d{4})-(0\d|1[0-2])-([0-2]\d|3[0-1]))", content).groups())