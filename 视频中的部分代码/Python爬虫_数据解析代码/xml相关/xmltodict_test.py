import xmltodict
import json

with open("test.xml", "r", encoding="utf-8") as f:
    result = xmltodict.parse(f.read())
    # print(result)
    # print(result["students"])

    json_str = json.dumps(result)
    # print(json_str)
    json_dict = json.loads(json_str,encoding="utf-8")
    print(json_dict)
    # xmltodict.OrderedDict

    print(xmltodict.unparse(json_dict))