import re

# 2019-06-01

# test_content = "2220-10-30"
# print(re.match("(\d{4})-(0\d|1[0-2])-([0-2]\d|3[0-1])", test_content).group(1))

content = """<a>xxxasd
fasd234234

顺子234dfx</a>"""
# print(re.match(r"<a>(.*)</a>", content).group(1))
# print(re.match(r"<a>([\w\W]*)</a>", content).group(1))

# print(re.match(r"<(\w+)>([\w\W]*)</\1>", content).group(2))

print(re.match(r"<(?P<the_tag>\w+)>([\w\W]*)</(?P=the_tag)>", content).group("the_tag"))


