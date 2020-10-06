import re

# test_str = """itlike"""
test_str = """6"""

pattern = "\d"
result = re.match(pattern, test_str)
if result:
    print(result.group())
# print(result)