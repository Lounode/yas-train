import random
import os

from PIL import Image, ImageFont, ImageDraw

from mona.text.artifact_name import random_artifact_name
from mona.text.stat import random_sub_stat, random_main_stat_name, random_main_stat_value
from mona.text.characters import random_equip
from mona.config import config
from mona.datagen.pre_process import pre_process
<<<<<<< HEAD
from mona.text.item import randomItemName
from mona.text.number import randomNumber

fonts = [ImageFont.truetype("./assets/genshin.ttf", i) for i in range(15, 40)]
=======

# 4k分辨率最大对应84号字，900p分辨率最小对应18号字
fonts = [ImageFont.truetype("./assets/genshin.ttf", i) for i in range(15, 90)]
>>>>>>> upstream/main


def random_level():
    return "+" + str(random.randint(0, 20))


def random_artifact_count():
    # Random here, for online learning
    flag_ac = random.randint(0, 1500)
    return f"圣遗物 {flag_ac}/1500"


<<<<<<< HEAD
random_funcs = [randomNumber]
#random_weights = [0.1, 0.05, 0.15,
#                  0.64, 0.02, 0.02, 0.02]
=======
random_funcs = [random_artifact_name, random_main_stat_name, random_main_stat_value,
                random_sub_stat, random_level, random_equip, random_artifact_count]
# 加大random_artifact_count的权重，因为连续数字识别是CRNN模型的难点，这对于副词条识别也有帮助。
random_weights = [0.1, 0.05, 0.15,
                  0.64, 0.02, 0.02, 0.1]
>>>>>>> upstream/main


def rand_color_1():
    r = random.randint(150, 255)
    g = random.randint(150, 255)
    b = random.randint(150, 255)

    # temp = random.choice(background_colors)
    # r = min(255, temp[0] + random.randint(-20, 20))
    # g = min(255, temp[1] + random.randint(-20, 20))
    # b = min(255, temp[2] + random.randint(-20, 20))

    return r, g, b


def rand_color_2():
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)

    # temp = random.choice(font_colors)
    # r = min(255, temp[0] + random.randint(-20, 20))
    # g = min(255, temp[1] + random.randint(-20, 20))
    # b = min(255, temp[2] + random.randint(-20, 20))

    return r, g, b


def random_text():
    func = random.choices(
        population=random_funcs,
        #weights=random_weights,
        k=1
    )
    return func[0]()


def generate_image():
    color1 = rand_color_1()
    color2 = rand_color_2()

    img = Image.new("RGB", (1200, 120), color1)
    # img = Image.new("RGB", (config["train_width"], config["height"]), color1)
    draw = ImageDraw.Draw(img)
    x = random.randint(0, 20)
    y = random.randint(0, 5)

    text = random_text()

    draw.text((x, y), text, color2, font=random.choice(fonts))

    # Random binarization thr to mimic various rendering
    thr = random.uniform(0.5, 0.6)
    img = pre_process(img, thr)
    # img = resize_to_32(img)
    # print(img.size)
    return img, text


# Generate and return sample before/after pre_process
def generate_image_sample():
    color1 = rand_color_1()
    color2 = rand_color_2()

    img = Image.new("RGB", (1200, 120), color1)
    draw = ImageDraw.Draw(img)
    x = random.randint(0, 20)
    y = random.randint(0, 5)

    text = random_text()
    # draw.text((x, y), text, color2, font=random.choice(fonts))

    # This would disable anit-aliasing
    # draw.fontmode = "1"

    draw.text((20, 5), "雷素%暴岩1,7.", color2, font=ImageFont.truetype("./assets/genshin.ttf", 80))

    img_processed = pre_process(img)
    return img, img_processed   
