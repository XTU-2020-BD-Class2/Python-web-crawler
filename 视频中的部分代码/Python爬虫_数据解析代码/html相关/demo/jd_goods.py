import requests
from bs4 import BeautifulSoup

def get_jd_goods(key):
    url = "https://search.jd.com/Search?keyword={}&enc=utf-8&wq=iphone".format(key)

    resp = requests.get(url, headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    })

    resp.encoding = "utf-8"
    # print(resp.text)

    # with open("test.html", "w", encoding="utf-8") as f:
    #     f.write(resp.text)

    soup = BeautifulSoup(resp.text, features="lxml")
    # 如果我们给的条件并不够精准， 结果数据不够唯一
    # 增加检索条件
    # 标签本身： 属性
    # 父节点（标签名称， 属性）
    # print(soup.find_all("i"))
    # print(soup.find_all("strong"))
    # divs = soup.find_all("div", attrs={"class": "p-price"})
    #
    # for div in divs:
    #     print(div.find("i").text)

    # titles = soup.find_all("div", attrs={"class": "p-name"})
    # for title in titles:
    #     print(title.find("em").text)
    #     print("https://" + title.find("a").get("href").split("//")[-1])

    # 1. 直奔目标
    # 2. 先自己： 属性（id, class, 其他属性）
    # 3. 父节点（标签名， 属性（id, class, 其他属性））
    # 4. 祖先节点（标签名， 属性（id, class, 其他属性））
    # print(soup.select("strong>i"))
    #
    # # print(soup.select("em"))
    # print(soup.select("a>em"))
    # for title in soup.select("div.p-name em"):
    #     print(title.text)
    #
    # for a in soup.select("div.p-name>a"):
    #     print("https://" + a.get("href").split("//")[-1])

    good_list = []
    for div in soup.select("div.gl-i-wrap"):
        good_dic = {}
        try:
            good_dic["price"] = float(div.select_one("div.p-price i").text)
        except Exception:
            good_dic["price"] = 0
        good_dic["name"] = div.select_one("div.p-name em").text
        good_dic["url"] = "https://" + div.select_one("div.p-name a").get("href").split("//")[-1]
        good_list.append(good_dic)
    return good_list