import pickle

def eat():
    print("sz在吃饭")

# dic = {
#     "name": "sz",
#     "age": 18,
#     "eat": eat
# }

# print(pickle.dumps(dic))
# with open("json_pickle.json", "wb") as f:
#     pickle.dump(dic, f)

with open("json_pickle.json", "rb") as f:
    result = pickle.load(f)
    print(result)
    # result["eat"]()