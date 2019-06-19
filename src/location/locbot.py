import datetime
import logging
import os
import time
import json
import dotenv
import gspread
import sys

import requests
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver


class LocBot:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dotenv.load_dotenv(os.path.join(BASE_DIR, '../../.env'))

    username = os.environ.get('LOGIN', ''),
    password = os.environ.get('PASSWORD', '')
    driver = webdriver.Firefox()

    ## Urls
    # Instagram
    insta_login_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

    ## Google Sheets
    # The city neighborhood  that you want to get.
    sheet_url = 'https://www.googleapis.com/auth/drive'
    sheet_name = 'Bairros - Cidade do RJ'

    ## Write_log
    log_mod = 0

    ## City
    city_name = 'Rio de Janeiro, Rio de Janeiro'

    def start(self):
        self.write_log('Starting Locbot')
        self.write_log('Opening browser')
        # Open Browser

        self.driver.get(self.insta_login_url)
        print('Locbot is trying login...')
        self.login()

    def login(self):
        # Find the login form
        while True:
            try:
                self.driver.find_element_by_xpath("//option[@value='en']").click()
                break
            except:
                pass

        while True:
            try:
                username_form = self.driver.find_element_by_xpath("//input[@aria-label='Phone number, username, or email']")
                password_form = self.driver.find_element_by_xpath("//input[@aria-label='Password']")
                break
            except:
                pass

        # Trying to sign in on Instagram
        try:
            username_form.send_keys(self.username)
            password_form.send_keys(self.password)
            self.driver.find_element_by_class_name('_0mzm-.sqdOP.L3NKy').click()
        except:
            self.driver.close()
            sys.exit('ERROR: Login or Password is invalid! Exiting...')

        if 'challenge' in self.driver.current_url:
            self.write_log('WARNING: Your account or IP is blocked \n'
                           'You will need to wait 24 hours to unlocked your account or IP adress')
            self.driver.close()
            sys.exit('ERROR: Instagram blocked you')
        else:
            self.write_log('Location Bot login success!')

        # All times that the Firefox open and the bot sign in the Instagram
        # it'll ask if you want to turn on the notifications.
        while True:
            try:
                self.driver.find_element_by_class_name('aOOlW.HoLwm').click()
                break
            except:
                pass
        self.search()

    def get_location(self):
        scope = [self.sheet_url]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('../../client_secret.json', scope)
        client = gspread.authorize(credentials)
        sheet = client.open('Locations and Hashtags').worksheet(self.sheet_name)
        response = sheet.get_all_records()

        locations = list(map(lambda l: l['location'], response))
        print(locations)

        return locations

    def search(self):
        locations = self.get_location()

        location = locations[0]

        if 'https://www.instagram.com/' == self.driver.current_url:
            search_form = self.driver.find_element_by_class_name('XTCLo.x3qfX')
            search_form.send_keys(location)
            place_list = []
            while True:
                time.sleep(1)
                if not place_list:
                    place_list = list(map(lambda l: l.get_attribute('href'), self.driver.find_elements_by_class_name('yCE8d  ')))
                else:
                    break

            for place in place_list:
                self.driver.get(place)
                location_name = self.driver.find_element_by_class_name('_7UhW9').text
                photos_list = self.driver.find_elements_by_xpath("//a[contains(@href, 'p')]")
                for photo in photos_list:
                    response = requests.get(photo.get_attribute('href') + '?__a=1')
                    result = response.json()
                    photos_list_size = photos_list.count()
                    address = json.loads(result['graphql']['shortcode_media']['location']['address_json'])
                    # if self.city_name == address['city_name']:
                    #     a = {'name': location, ''}



    def write_log(self, log_text):
        """ Write log by print() or logger """

        if self.log_mod == 0:
            try:
                now_time = datetime.datetime.now()
                print(now_time.strftime("%d.%m.%Y_%H:%M")  + " " + log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")
        elif self.log_mod == 1:
            # Create log_file if not exist.
            if self.log_file == 0:
                self.log_file = 1
                now_time = datetime.datetime.now()
                self.log_full_path = '%s%s_%s.log' % (
                    self.log_file_path, self.user_login,
                    now_time.strftime("%d.%m.%Y_%H:%M"))
                formatter = logging.Formatter('%(asctime)s - %(name)s '
                                              '- %(message)s')
                self.logger = logging.getLogger(self.user_login)
                self.hdrl = logging.FileHandler(self.log_full_path, mode='w')
                self.hdrl.setFormatter(formatter)
                self.logger.setLevel(level=logging.INFO)
                self.logger.addHandler(self.hdrl)
            # Log to log file.
            try:
                self.logger.info(log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")







loc = LocBot()
loc.start()