import json
import re
import time
import requests

path = 'https://small-big-api.herokuapp.com/photo'


def add_hashtag(shortcode, hashtag):
    try:
        data = {
            'shortcode': shortcode,
            'hashtag': hashtag
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = json.dumps(data)
        r = requests.patch(path + '/' + shortcode, data=data, headers=headers)
    except:
        r = 0
    print(shortcode, r)
    return r


def get_hashtag(text):
    hashtags = re.findall(r"#(\w+)", text)
    return hashtags


def update_all_hashtag():
    response = requests.get(path, stream=False)
    result = response.json()
    for small_big in result['result']:
        time.sleep(5)
        try:
            text = small_big['text']
            add_hashtag(small_big['shortcode'], get_hashtag(text))
        except:
            print(f"Warning: image: {small_big['shortcode']}. This page isn't available.")
            add_hashtag(small_big['shortcode'], None)


#update_all_hashtag()
