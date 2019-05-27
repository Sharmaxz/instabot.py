import time
import requests

path = 'https://small-big-api.herokuapp.com/photo/processed'


def delete_all_duplicate():
    time.sleep(5)
    response = requests.get(path, stream=False)
    result = response.json()

    list_shortcode = list(map(lambda _obj: _obj['shortcode'], result['result']))
    shortcode_duplicated = list(set([x for x in list_shortcode if list_shortcode.count(x) > 1]))

    for shortcode in shortcode_duplicated:
        requests.delete(path + '/delete/' + shortcode)
        print(f'{shortcode} was deleted!')
    delete_all_duplicate()



delete_all_duplicate()
