from jsonpath import jsonpath

dic = {

    "person": {
        "name": "sz",
        "age": 18,
        "dog": [{
            "name": "小花",
            "color": "red",
            "age": 6,
            "isVIP": True
        },
        {
            "name": "小黑",
            "color": "black",
            "age": 2
        }]
    }
}

# print(dic["person"]["dog"][0]["age"])

# result = jsonpath(dic, "$.person.age")
# result = jsonpath(dic, "$.person.dog[1].age")
# result = jsonpath(dic, "$..dog[1].age")
# result = jsonpath(dic, "$..dog[0,1].age")
# result = jsonpath(dic, "$..dog[*].age")
# result = jsonpath(dic, "$..dog[?(@.isVIP)]")
# result = jsonpath(dic, "$..dog[?(@.age < 3)]")
result = jsonpath(dic, "$..dog[(@.length-1)]")
print(result)
print(type(result))