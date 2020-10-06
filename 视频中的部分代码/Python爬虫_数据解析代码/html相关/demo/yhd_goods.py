import requests
from bs4 import BeautifulSoup

def get_yhd_goods(key):
    url = "https://search.yhd.com/c0-0/k" + key

    resp = requests.get(url)

    # print(resp.text)

    # with open("yhd.html", "w", encoding="utf-8") as f:
    #     f.write(resp.text)

    soup = BeautifulSoup(resp.text, features="lxml")

    # ems = soup.select("p.proPrice>em.num")
    # for em in ems:
    #     # print(em.text)
    #     print(list(em.stripped_strings)[-1])


    # titles = soup.select("a.mainTitle")
    #
    # # print(titles)
    #
    # for title in titles:
    #     print(title.get("title"))
    #     print("https:" + title.get("href"))
        # print(list(title.stripped_strings)[-1])
        # print(list(title.select_one("style").next_siblings)[-1])

    good_list = []

    divs = soup.select("div.mod_search_pro>div.itemBox")
    for div in divs:
        good_dic = {}
        try:
            good_dic["price"] = float(list(div.select_one("p.proPrice>em.num").stripped_strings)[-1])
        except Exception:
            good_dic["price"] = 0
        # print(price)
        # print("-"*30)
        # print(div)
        good_dic["name"] = div.select_one("p.proName>a[title]").get("title")
        # print(title)

        good_dic["url"] = "https:" + div.select_one("p.proName>a[title]").get("href")
        # print(url)
        good_list.append(good_dic)

    return good_list