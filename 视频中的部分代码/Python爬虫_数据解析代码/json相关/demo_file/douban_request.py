import requests as rt
from jsonpath import jsonpath

def get_movies():

    # get
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=60&page_start=0"


    resp = rt.get(url)

    # print(resp.text)

    # import json
    # result = json.loads(resp.text, encoding="utf-8")
    # print(type(result))
    # print(result)


    result = resp.json()
    print(type(result))
    # print(result)

    # tmp = []
    # for dic in result["subjects"]:
    #     if float(dic["rate"]) >= 8.0:
    #         tmp.append(dic)
    # print(tmp)
    #
    # tmp = [dic for dic in result["subjects"] if float(dic["rate"]) >= 8.0]
    # print(tmp)



    # movies = jsonpath(result, "$.subjects[?(float(@.rate)>=8.0 && @.playable==True)].cover")
    # movies = jsonpath(result, "$.subjects[?(float(@.rate)>=8.0 && @.playable==True)]['cover','title']")
    movies = jsonpath(result, "$.subjects[?(float(@.rate)>=8.0 && @.playable==True)]")
    # print(movies)

    movie_result = []
    for movie_dic in movies:
        new_movie = {}
        new_movie["title"] = movie_dic["title"]
        new_movie["score"] = movie_dic["rate"]
        # del movie_dic["cover_x"]
        # del movie_dic["cover_y"]
        # del movie_dic["is_new"]
        # del movie_dic["url"]

        image_url = movie_dic["cover"]
        image_resp = rt.get(image_url)
        image_path = "movie_images/{}.jpg".format(movie_dic["id"])
        with open(image_path, "wb") as f:
            f.write(image_resp.content)
        new_movie["image_path"] = image_path
        movie_result.append(new_movie)

    return  movie_result
