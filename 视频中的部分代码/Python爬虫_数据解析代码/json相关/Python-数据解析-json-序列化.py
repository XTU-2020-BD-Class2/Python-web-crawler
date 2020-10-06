import json

# 序列化操作
# 对象：字典 列表  -》 json字符串

class Phone:
    def __init__(self, name, price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.price = price


obj1 = {}
obj2 = {}
obj1["value"] = obj2
obj2["value"] = obj1

dic = {
    "name": "sz",
    "age": 18,
    # (1, 2): 666,
    # "circle": obj1,
    # "n": float('nan'),
    "phone": Phone("is6", "888"),
    "dog": {
        "name": "煤球",
        "age": 2,
        "color": "黑色",
        "isVIP": True,
        "child": None
    }
}


class Default(json.JSONEncoder):
    def default(self, o):
        print(o)
        return [o.name, o.price]


# result = json.dumps(dic, skipkeys=True, ensure_ascii=False, check_circular=False, allow_nan=False)
# result = json.dumps(dic, cls=Default, indent=4)
def parse(obj):
    print(obj)
    return {"name": obj.name, "price": obj.price}

# result = json.dumps(dic, indent=4, default=parse, sort_keys=True)
with open("json2file.json", "w", encoding="utf-8") as f:

    result = json.dump(dic, fp=f, indent=4, default=parse, sort_keys=True, ensure_ascii=False)
    print(type(result))
    print(result)