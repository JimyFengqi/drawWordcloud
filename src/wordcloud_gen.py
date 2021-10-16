import os
import platform

import jieba
import numpy as np
from PIL import Image, ImageTk
from wordcloud import WordCloud


def get_font():
    font_dir = "C:\\Windows\\Fonts"
    return os.path.join(font_dir, os.listdir(font_dir)[-1])


def get_text(fn):
    """
    读取用户提供的文件
    """
    return open(fn, "r", encoding="utf-8").read()


def get_text_cn(text):
    """
    将文字通过jieba进行分词
    """
    return " ".join(jieba.cut(text, cut_all=False))


def generator_cloud_image(file_path, image_path):
    file_text = get_text(file_path)
    text = get_text_cn(file_text)
    mask = np.array(Image.open(image_path))
    os_platform = platform.platform()
    if os_platform[0] == "W":
        wc = WordCloud(
            max_words=2000,
            font_path=get_font(),
            mask=mask,
            max_font_size=400,
            random_state=420,
            margin=0,
        ).generate(text)
    else:
        wc = WordCloud(
            max_words=2000,
            mask=mask,
            max_font_size=400,
            random_state=420,
            margin=0,
        ).generate(text)
    im = wc.to_image()
    # im.show()
    new_word_cloud_image = image_path.split(".")[0] + "word_cloud.jpg"
    im.save(new_word_cloud_image)

    return new_word_cloud_image


def handle_picture(pic):
    im = Image.open(pic)
    w, h = im.size
    # 这里假设用来显示图片的Label组件尺寸为400*600
    if w > 400:
        h = int(h * 400 / w)
        w = 400
    if h > 600:
        w = int(w * 600 / h)
        h = 600
    resize_image = im.resize((w, h))
    photo = ImageTk.PhotoImage(resize_image)
    return photo
