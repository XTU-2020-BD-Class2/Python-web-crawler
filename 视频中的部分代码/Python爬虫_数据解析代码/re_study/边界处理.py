import re

# 1 2 10数字
# 2 - 35678
# print(re.match("1\d{10}", """10111111111"""))
# print(re.match("1[35-8]\d{9}", """17111111111"""))


# print(re.match("1[35-8]\d{9}$", """a17111111111"""))


# 左  右
# 1 没有匹配到 ->
# print(re.findall("^1[35-8]\d{9}$", """17111111111bc"""))

# c:\\abc\g\test.py

# python 特殊的转移符 \特殊的字符

# test_str = "c:\\abc\g\test.py"
# test_str = "c:\\\\abc\\g\\test.py"
test_str = r"c:\\abc\g\test.py"
# print(test_str)


#
# print(re.match("\w", "6"))

# 1. 两个参数类型是什么类型? str(普通 原始) \n
# re.match("\a", "")


# print(re.match("a", "a"))
# print(re.match("\a", "\a"))
# print(re.match("\\\\d", "\d"))


# 1. 先按照普通的python字符串进行转义
    # 2. 如果说不能够被python字符串进行转义, 那么就尝试按照正则表达式的规则进行转义
    # 3. 如果按照正则表达式的转义进行处理, 还是不能转义, 那么就直接报错
# 4. 按照正则的规则来进行匹配

# c:\\\\\\\\abc\\\\g\\\\test.py
# c:\\\\abc\\g\test.py
#

# print(re.match("c:\\\\\\\\abc\\\g\\\\test.py", "c:\\\\abc\g\\test.py"))


# print(re.match("c:\\\\\\\\abc\\\d\\\\test.py", "c:\\\\abc\d\\test.py"))

# print(re.match(r"c:\\\\abc\\d\\test.py", "c:\\\\abc\d\\test.py"))


# print(re.match("\\\\a", r"\a"))
# print(re.match(r"\\a", r"\a"))

# 1. \n
#
#


# print(re.match("\\n", "\n"))

# "\\\\d"
# 1. "\\d"

# 4. \d
# print(re.match("\\\d", "\d"))



# test_str = "ab likeit it! itlike! cd xx."

# print(re.findall(r"\bit\B", test_str))
# print(re.findall(r"\Bit\b", test_str))
# print(re.findall(r"\b\w{2}\b", test_str))





