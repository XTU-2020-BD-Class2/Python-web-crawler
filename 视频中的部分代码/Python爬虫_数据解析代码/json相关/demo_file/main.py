from douban_vx import vx, send_image
from douban_request import get_movies
from douban_pil import hc_image

if __name__ == '__main__':
    def itlike_do():
        movies = get_movies()
        for movie in movies:
            # print(movie)
            image_path = hc_image(movie["image_path"], movie["title"], movie["score"], movie["image_path"])
            send_image(image_path)
    vx("itlike", itlike_do)