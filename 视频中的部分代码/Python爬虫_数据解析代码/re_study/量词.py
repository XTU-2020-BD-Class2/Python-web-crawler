import re

# 简单的手机号
# 12345678901
# 规则: 1后边 10位必须是数字
# print(re.match("1\d\d\d\d\d\d\d\d\d\d", """12345678901"""))

# print(re.match("1\d{10}", """12345678a01"""))

# print(re.match("\d*", """"""))

# print(re.match("\d+", """1234567a789"""))
# print(re.match("\d?", """12"""))
# print(re.match("\d{2,}", """1234a"""))
# print(re.match("\d{2,4}", """1a"""))




