import time
from PIL import Image
from colorsys import rgb_to_hls
import os
import requests
import json
from collections import namedtuple

path = 'https://small-big-api.herokuapp.com/photos/'


def add_colors(shortcode, rgbhsl):
    try:
        data = {
            'shortcode': shortcode,
            'red': rgbhsl.r,
            'green': rgbhsl.g,
            'blue': rgbhsl.b,
            'hue': rgbhsl.h,
            'saturation': rgbhsl.s,
            'lightness': rgbhsl.l,
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = json.dumps(data)
        r = requests.patch('https://small-big-api.herokuapp.com/photo/'+shortcode, data=data, headers=headers)
    except:
        r = 0
    print(shortcode, rgbhsl, r)
    return r


def img_rgbhsl_rep(img):
    RGBHSL = namedtuple('RGBHSL', ['r', 'g', 'b', 'h', 's', 'l'])
    image_colors = img.getcolors(maxcolors=1000000)
    total_occurences, red_rep, green_rep, blue_rep = 0, 0, 0, 0
    for color in image_colors:
        total_occurences += color[0]
        red_rep += color[1][0] * color[0]
        green_rep += color[1][1] * color[0]
        blue_rep += color[1][2] * color[0]
    rgb_rep = (int(red_rep / total_occurences), int(green_rep / total_occurences), int(blue_rep / total_occurences))
    (hue, saturation, lightness) = rgb_to_hls(*rgb_rep)
    return RGBHSL(rgb_rep[0], rgb_rep[1], rgb_rep[2], hue, saturation, lightness)


# 'src/extract_color/imgs'
# for image in os.listdir('src/extract_color/imgs'):
#     time.sleep(5)
#     HUE, R, G, B = [], [], [], []
#     response = requests.get(path + image, stream=False)
#     result = response.json()
#     if not 'red' in result and not 'green' in result and not'blue' in result:
#         if image.endswith('.jpg'):
#             try:
#                 img = Image.open(f'imgs/{image}').convert('RGB')
#                 rgbhsl = img_rgbhsl_rep(img)
#                 add_colors(image.replace('.jpg', ''), rgbhsl)
#             except OSError:
#                 pass
