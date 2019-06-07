import time

import requests

path = 'http://small-big-api.herokuapp.com/photo/processed'
response = requests.get(path, stream=False)
result = response.json()
img_count, img_reponse_failed = 0, 0
for small_big in result['result']:
    time.sleep(5)
    with open('imgs/'+small_big['shortcode'] + '.jpg', 'wb') as handle:
        img_count += 1
        print(small_big['shortcode'])
        response = requests.get(small_big['image_url'], stream=True)
        if not response.ok:
            img_reponse_failed += 1
            delete = requests.delete(path + '/delete/' + small_big['shortcode'])
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

    img_percent = img_reponse_failed / img_count
    print(f'Downloaded images status:\n'
          f'{"%.2f"%(img_percent)}% failed | '
          f'{"%.2f"%(100 - img_percent)}% completed | '
          f'images total: {img_count}')
