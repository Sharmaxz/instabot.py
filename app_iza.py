#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import dotenv
from src.location.extract_location import get_locations_id


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

from src import InstaBot

location_ids = get_locations_id('IZABELLA')

if __name__ == '__main__':

    bot = InstaBot(
        login=os.environ.get('IZALOGIN', ''),
        password=os.environ.get('IZAPASSWORD', ''),
        like_per_day=1400,
        comments_per_day=0,
        tag_list=[id['location_id'] for id in location_ids][::-2],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=0,
        follow_time=1 * 60,
        unfollow_per_day=0,
        unfollow_break_min=15,
        unfollow_break_max=30,
        log_mod=0,
        proxy='',
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[["this", "the", "your"],
                      ["photo", "picture", "pic", "shot", "snapshot"],
                      ["is", "looks", "feels", "is really"],
                      ["great", "super", "good", "very good", "good", "wow",
                       "WOW", "cool", "GREAT", "magnificent", "magical",
                       "very cool", "stylish", "beautiful", "so beautiful",
                       "so stylish", "so professional", "lovely",
                       "so lovely", "very lovely", "glorious","so glorious",
                       "very glorious", "adorable", "excellent", "amazing"],
                      [".", "..", "...", "!", "!!", "!!!"]],
        # Use unwanted_username_list to block usernames containing a string
        ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
        ### 'free_followers' will be blocked because it contains 'free'
        unwanted_username_list=[
            'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
            'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
            'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
            'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
            'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
            'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
            'follow', 'follower', 'gain', '.id', '_id', 'bags'
        ],
        unfollow_whitelist=['example_user_1', 'example_user_2'])

    while True:

        mode = 0

        if mode == 0:
            bot.auto_mod()
