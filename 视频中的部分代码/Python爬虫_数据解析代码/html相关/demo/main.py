from jd_goods import get_jd_goods
from yhd_goods import get_yhd_goods

if __name__ == '__main__':
    key = input("请输入你要检索的商品关键字：")
    jds = get_jd_goods(key)
    yhds = get_yhd_goods(key)

    new_goods = jds + yhds
    # print(new_goods)
    def get_price(dic):
        return dic["price"]

    print(sorted(new_goods, key=get_price)[0])