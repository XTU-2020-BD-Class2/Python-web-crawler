import re

# print(re.match("\d", "0"))
# print(re.match("\d", "a"))
# print(re.match(".", "a"))
# print(re.match(".", "="))
# print(re.match(".", "0"))
# print(re.match(".", "顺"))
# print(re.match(".", """
# """))

# print(re.match("\d", "0.9"))
# print(re.match("\D", "2"))


# print(re.match("\s", """1"""))

# print(re.match("\w", """_"""))

# print(re.match("[^itlke]", """a"""))
# print(re.match("[itlke]", """a"""))
# print(re.match("[c-z]", """z"""))
# print(re.match("[c-zD-G]", """D"""))

# print(re.match("\d\d", """11"""))
# print(re.match("[a-z]\d", """cc"""))
# print(re.match("[a-z][A-Z]", """cC"""))

print(re.match("[\w\W]", """9"""))
