import time
import requests
import json


def update_to_api_small_big(shortcode, timestamp):
    try:
        data = {
            'shortcode': shortcode,
            'taken_at_timestamp': timestamp
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = json.dumps(data)
        r = requests.patch('https://small-big-api.herokuapp.com/photo/'+shortcode, data=data, headers=headers)
    except:
        r = 0
    print(shortcode, r)
    return r


path = 'https://small-big-api.herokuapp.com/photo'
response = requests.get(path, stream=False)
result = response.json()

for small_big in result['result']:
    time.sleep(5)
    if not 'taken_at_timestamp' in small_big or 'none' in small_big:
        url = f'https://instagram.com/p/{small_big["shortcode"]}/?__a=1'
        r = requests.get(url, stream=False)
        try:
            result1 = r.json()
            timestamp = result1['graphql']['shortcode_media']['taken_at_timestamp']
            print(f'{small_big["shortcode"]}, timestamp: {timestamp}')
            update_to_api_small_big(small_big['shortcode'], timestamp)
        except:
            print(f"Warning: image: {small_big['shortcode']}. This page isn't available.")
            update_to_api_small_big(small_big['shortcode'], None)
