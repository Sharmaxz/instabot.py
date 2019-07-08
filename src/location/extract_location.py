from oauth2client.service_account import ServiceAccountCredentials
import gspread
import requests
import json
import time

url = 'https://small-big-api.herokuapp.com/photo'
#url = 'http://127.0.0.1:5000/photo'
path = 'processed'
instagram_url = 'https://www.instagram.com/p/'
url_postmon = 'http://api.postmon.com.br/v1/cep/'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def add_location(shortcode, data):
    try:
        data = {
            'shortcode': shortcode,
            'location': data
        }
        data = json.dumps(data)
        r = requests.patch(url + '/' + shortcode, data=data, headers=headers)
    except:
        r = 0
    print(f"{shortcode} was updated! {r}")
    return r


def get_location(shortcode):
    insta_url = instagram_url + f'{shortcode}/?__a=1'
    insta_response = requests.get(insta_url, stream=False)
    insta_result = insta_response.json()
    id = insta_result['graphql']['shortcode_media']['location']['id']
    name = insta_result['graphql']['shortcode_media']['location']['name']
    address_json = insta_result['graphql']['shortcode_media']['location']['address_json']
    address = json.loads(address_json)

    response = requests.get(url_postmon + address['zip_code'], stream=False)
    if not response.ok and 'rio de janeiro' in address['city_name'].split(', ')[1].lower():
        zone = address['city_name'].split(', ')[0]
    else:
        r = response.json()
        if 'RJ' in r['estado']:
            zone = r['bairro']
        else:
            return print(a)

    return {'id': id, 'name': name, 'address_json': address_json, 'zone': zone}


def update_all_location():
    response = requests.get(url + '/' + path, stream=False)
    result = response.json()
    for small_big in result['result']:
        #time.sleep(5)
        try:
            data = get_location(small_big['shortcode'])
            add_location(small_big['shortcode'], data)
        except:
            r = requests.delete(url + '/delete/' + small_big['shortcode'], headers=headers)
            print(f"Warning: image: {small_big['shortcode']} can not updated. {r}")


# Used by app.py
def get_locations_id(name):
    name = name.upper()
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Locations and Hashtags').worksheet('Hashtags')
    result = sheet.get_all_records()
    location_filtered = [l for l in result if name in l['runner']]
    format = list(map(lambda obj: {'location_id': f"l:{obj['id']}", 'name': obj['location']}, location_filtered))

    return format


update_all_location()
