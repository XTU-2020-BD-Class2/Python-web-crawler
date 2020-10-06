

def hecheng(image_path, title, score, save_path):
    # 合成图片
    from PIL import Image, ImageDraw, ImageFont
    # 1. 打开背景图片
    back_image = Image.open("movie_back.jpg")
    tmp_img = Image.open(image_path)
    tmp_img = tmp_img.resize((600, 800))
    w,h = back_image.size
    box_left = (w - 600) // 2
    box_top = 400
    box_right = box_left + 600
    box_bottom = box_top + 800
    box = (box_left, box_top, box_right, box_bottom)
    back_image.paste(tmp_img, box)

    font_size = 130
    if len(title) * font_size > 600:
        font_size = 600 // len(title)

    draw = ImageDraw.Draw(back_image)
    title_font = ImageFont.truetype("hd.ttf", font_size)
    draw.text(((w - len(title) * font_size) // 2, 170), title, font=title_font)

    # 评分
    rate = score
    rate_font_size = 80
    rate_font = ImageFont.truetype("tx.ttf", rate_font_size)
    draw.text(((w - (len(rate) - 1) * rate_font_size) // 2, h - 200), rate, anchor=(0.5, 0.5), font=rate_font)

    back_image.save(save_path)



def down_load_file():
    import requests
    from jsonpath import jsonpath
    result = requests.get("https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0")
    movies = result.json()

    # print(movies)
    movie_dic_list = jsonpath(movies, "$..subjects[?(float(@.rate)>8.0 && @.playable==True)]")
    print(movie_dic_list)
    # keys = ["cover_x", "cover_y", "url", "playable", "is_new"]
    # for movie_dic in movie_dic_list:
    #     for key in keys:
    #         movie_dic.pop(key)

    return None
    images = []

    # 下载图片
    for movie in movie_dic_list:
        movie_id = movie["id"]
        movie_image = movie["cover"]
        movie_title = movie["title"]
        movie_score = movie["rate"]

        # 下载图片
        movie_image_data = requests.get(movie_image).content
        file_path = "movie_images/{}.jpg".format(movie_id)
        with open(file_path, "wb") as f:
            f.write(movie_image_data)

        hecheng(file_path, movie_title, movie_score, save_path=file_path)
        images.append(file_path)
    return images


down_load_file()

# 一、监听自己的微信“文件助手消息”
import itchat

# 1. 登录
# itchat.auto_login()
#
#
# # 2. 监听微信好友助手消息-文本
# @itchat.msg_register(itchat.content.TEXT)
# def txt_msg(msg):
#     # print(msg)
#     if msg["ToUserName"] == "filehelper":
#         if msg["Content"] == "itlike":
#             images = down_load_file()
#             for image in images:
#                 itchat.send_image(image, toUserName="filehelper")
#
# # 3. 运行
# itchat.run(True)