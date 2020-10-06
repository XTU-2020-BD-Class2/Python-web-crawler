
a = "aaa"
print(type(a))

l = [1, 2, "a"]
print(type(l))


d = {"name": "sz", "Age": 18}
print(type(d))

other = '{"name": "sz", "Age": 18}'
other = '[1, 2, "a"]'
print(type(other))


from urllib import request

url = "https://www.toutiao.com/stream/widget/local_weather/data/?city=%E5%8C%97%E4%BA%AC"
resp = request.urlopen(url)
print(type(resp.read().decode("utf-8")))

# print("wangshunzi")

# 一个人
"""
<person class="1">
    <id>001</id>
    <name>sz</name>
</person>
"""

"""
{
    "id": 001,
    "name": "sz"
}
"""

# 轻量级的数据交互格式




