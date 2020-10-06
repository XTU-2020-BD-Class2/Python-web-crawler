import json

# 反序列化操作
# 对象：json字符串 -》 字典 列表

class Phone:
    def __init__(self, name, price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.price = price

def oh(dic):
    print(dic)
    if "price" in dic.keys():
        phone = Phone(dic["name"], dic["price"])
        return phone
    return dic

def pi(num):
    return int(num) + 1


def oph(*args, **kwargs):
    print(*args, **kwargs)

with open("json2file.json", "r", encoding="utf-8") as f:
    # content = f.read()
    # result = json.loads(content, object_hook=oh, parse_int=pi)
    # result = json.loads(content, object_pairs_hook=oph)

    result = json.load(f, object_hook=oh, parse_int=pi)

    print(result)
    print(type(result))

