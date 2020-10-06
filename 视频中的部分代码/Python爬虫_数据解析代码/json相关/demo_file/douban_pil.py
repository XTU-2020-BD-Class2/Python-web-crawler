from PIL import Image, ImageDraw, ImageFont


def hc_image(movie_image_path, title, score_str, save_path):
    # 1. 先准备两个图片（背景，前景：电影）
    back_image = Image.open("movie_back.jpg")
    movie_image = Image.open(movie_image_path)
    movie_image = movie_image.resize((600, 800))

    # 2. 把电影图片绘制到背景图片上边
    w,h = back_image.size
    box = ((w - 600) // 2, 400)

    back_image.paste(movie_image, box=box)

    # 3. 在背景图片上边绘制文字
    back_image_draw = ImageDraw.Draw(back_image)
    title_font_size = 130
    title_font_w = title_font_size * len(title)
    if title_font_w > 600:
        title_font_size = 600 // len(title)
        title_font_w = title_font_size * len(title)
    title_font = ImageFont.truetype("title_font.ttf", title_font_size)

    back_image_draw.text(((w - title_font_w) // 2, 150), title, font=title_font)


    # 评分
    score = "评分：" + score_str
    score_size = 80
    score_font_w = score_size * len(score)
    score_font = ImageFont.truetype("score_font.ttf", score_size)

    back_image_draw.text(((w - score_font_w) // 2, h - 200), score, font=score_font)


    # 4. 保存处理好的背景图片
    back_image.save(save_path)
    return save_path