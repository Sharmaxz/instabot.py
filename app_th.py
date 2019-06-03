#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

from src import InstaBot

location_ids = [
{'location_id': '119999494746573', 'name': 'Paquetá, Rio de Janeiro, Brazil'},
{'location_id': '324148104', 'name': 'Galeão, Rio de Janeiro, Brazil'},
{'location_id': '370287903', 'name': 'Vila Kosmos, Rio de Janeiro, Brazil'},
{'location_id': '619566582', 'name': 'Vila Cosmos, Rio de Janeiro, Brazil'},
{'location_id': '213588142', 'name': 'Marechal Hermes, Rio de Janeiro, Brazil'},
{'location_id': '217589180', 'name': 'Vicente de Carvalho, Rio de Janeiro, Brazil'},
{'location_id': '370706375', 'name': 'Paciência, Rio de Janeiro, Brazil'},
{'location_id': '235061786', 'name': 'Engenho Da Rainha, Rio de Janeiro, Brazil'},
{'location_id': '474725268', 'name': 'Complexo do Alemão, Rio de Janeiro, Brazil'},
{'location_id': '243454557', 'name': 'Vaz Lobo, Rio de Janeiro, Brazil'},
{'location_id': '215789899', 'name': 'Padre Miguel, Rio de Janeiro, Brazil'},
{'location_id': '505018022', 'name': 'Bento Ribeiro, Rio de Janeiro, Brazil'},
{'location_id': '20737678', 'name': 'Turiaçu, Rio de Janeiro, Brazil'},
{'location_id': '225443570', 'name': 'Boncucesso, Rio de Janeiro, Brazil'},
{'location_id': '219393343', 'name': 'Boncucesso, Rio de Janeiro, Brazil'},
{'location_id': '297966939', 'name': 'Inhaúma, Rio de Janeiro, Brazil'},
{'location_id': '237512663', 'name': 'Tomás Coelho, Rio de Janeiro, Brazil'},
{'location_id': '297966939', 'name': 'Inhaúma, Rio de Janeiro, Brazil'},
{'location_id': '237512663', 'name': 'Tomás Coelho, Rio de Janeiro, Brazil'},
{'location_id': '244305931', 'name': 'Santíssimo, Rio de Janeiro, Brazil'},
{'location_id': '223589801', 'name': 'Madureira, Rio de Janeiro, Brazil'},
{'location_id': '644923990', 'name': 'Oswaldo Cruz, Rio de Janeiro, Brazil'},
{'location_id': '213340181', 'name': 'Santa Cruz, Rio de Janeiro, Brazil'},
{'location_id': '235203259', 'name': 'Magalhães Bastos, Rio de Janeiro, Brazil'},
{'location_id': '220783438', 'name': 'Senador Camará, Rio de Janeiro, Brazil'},
{'location_id': '317349667', 'name': 'Cavalcanti, Rio de Janeiro, Brazil'},
{'location_id': '235219908', 'name': 'Campo dos Afonsos, Rio de Janeiro, Brazil'},
{'location_id': '271772743', 'name': 'Campo dos Afonsos, Rio de Janeiro, Brazil'},
{'location_id': '228857941', 'name': 'Higienópolis, Rio de Janeiro, Brazil'},
{'location_id': '6958763', 'name': 'Higienópolis, Rio de Janeiro, Brazil'},
{'location_id': '254896886', 'name': 'Manguinhos, Rio de Janeiro, Brazil'},
{'location_id': '13886195', 'name': 'Engenheiro Leal, Rio de Janeiro, Brazil'},
{'location_id': '229508750', 'name': 'Pilares, Rio de Janeiro, Brazil'},
{'location_id': '229364788', 'name': 'Del Castilho, Rio de Janeiro, Brazil'},
{'location_id': '513138999', 'name': 'Piedade, Rio de Janeiro, Brazil'},
{'location_id': '218955154', 'name': 'Cascadura, Rio de Janeiro, Brazil'},
{'location_id': '215659485', 'name': 'Vila Valqueire, Rio de Janeiro, Brazil'},
{'location_id': '224849782', 'name': 'Maria da Graça, Rio de Janeiro, Brazil'},
{'location_id': '242047776', 'name': 'Quintino Bocaiúva, Rio de Janeiro, Brazil'},
{'location_id': '498626754', 'name': 'Jardim Sulacap, Rio de Janeiro, Brazil'},
{'location_id': '215799724', 'name': 'Jardim Sulacap, Rio de Janeiro, Brazil'},
{'location_id': '250651732', 'name': 'Campinho, Rio de Janeiro, Brazil'},
{'location_id': '447075808', 'name': 'Abolição, Rio de Janeiro, Brazil'},
{'location_id': '235134557', 'name': 'Senador Vasconcelos, Rio de Janeiro, Brazil'},
{'location_id': '214704422', 'name': 'Cosmos, Rio de Janeiro, Brazil'},
{'location_id': '372952224', 'name': 'Jacarezinho, Rio de Janeiro, Brazil'},
{'location_id': '237956912', 'name': 'Cachambi, Rio de Janeiro, Brazil'},
{'location_id': '219626708', 'name': 'Praça Seca, Rio de Janeiro, Brazil'},
{'location_id': '327146338', 'name': 'Benfica, Rio de Janeiro, Brazil'},
{'location_id': '621830528237318', 'name': 'Engenho de Dentro, Rio de Janeiro, Brazil'},
{'location_id': '749841000', 'name': 'Imperial de São Cristovão, Rio de Janeiro, Brazil'},
{'location_id': '609573734', 'name': 'Vasco da Gama, Rio de Janeiro, Brazil'},
{'location_id': '244097158', 'name': 'Inhoaíba, Rio de Janeiro, Brazil'},
{'location_id': '248703424', 'name': 'Todos os Santos, Rio de Janeiro, Brazil'},
{'location_id': '221313789', 'name': 'Jacaré, Rio de Janeiro, Brazil'},
{'location_id': '234599175', 'name': 'Encantado, Rio de Janeiro, Brazil'},
{'location_id': '753897135', 'name': 'Rocha, Rio de Janeiro, Brazil'},
{'location_id': '216348954', 'name': 'Méier, Rio de Janeiro, Brazil'},
{'location_id': '505870750', 'name': 'Gamboa, Rio de Janeiro, Brazil'},
{'location_id': '240419404', 'name': 'Santo Cristo, Rio de Janeiro, Brazil'},
{'location_id': '731003687', 'name': 'Centro, Rio de Janeiro, Brazil'},
{'location_id': '261277779', 'name': 'Sampaio, Rio de Janeiro, Brazil'},
{'location_id': '238414735', 'name': 'Riachuelo, Rio de Janeiro, Brazil'},

{'location_id': '238512597', 'name': 'Andaraí, Rio de Janeiro, Brazil'},
{'location_id': '238123296', 'name': 'Catete, Rio de Janeiro, Brazil'},
{'location_id': '224254831', 'name': 'Flamengo, Rio de Janeiro, Brazil'},
{'location_id': '1863813143871730', 'name': 'Laranjeiras, Rio de Janeiro, Brazil'},
{'location_id': '254693080', 'name': 'Guaratiba, Rio de Janeiro, Brazil'},
{'location_id': '257453801', 'name': 'Vargem Grande, Rio de Janeiro, Brazil'},
{'location_id': '214993240', 'name': 'Alto da Boa Vista, Rio de Janeiro, Brazil'},
{'location_id': '219637024', 'name': 'Cosme Velho, Rio de Janeiro, Brazil'},
{'location_id': '229688043', 'name': 'Curicica, Rio de Janeiro, Brazil'},
{'location_id': '213396483', 'name': 'Botafogo, Rio de Janeiro, Brazil'},
{'location_id': '229165580', 'name': 'Urca, Rio de Janeiro, Brazil'},
{'location_id': '317148057', 'name': 'Cidade de Deus, Rio de Janeiro, Brazil'},
{'location_id': '240377209', 'name': 'Sepetiba, Rio de Janeiro, Brazil'},
{'location_id': '214220409', 'name': 'Anil, Rio de Janeiro, Brazil'},]

if __name__ == '__main__':

    bot = InstaBot(
        login=os.environ.get('TH_LOGIN', ''),
        password=os.environ.get('TH_PASSWORD', ''),
        like_per_day=1400,
        comments_per_day=0,
        tag_list=['l:' + id['location_id'] for id in location_ids][::2],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=0,
        follow_time=1 * 60,
        unfollow_per_day=0,
        unfollow_break_min=15,
        unfollow_break_max=30,
        log_mod=0,
        proxy='',
        database_name='th_follows_db.db',
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[["this", "the", "your"],
                      ["photo", "picture", "pic", "shot", "snapshot"],
                      ["is", "looks", "feels", "is really"],
                      ["great", "super", "good", "very good", "good", "wow",
                       "WOW", "cool", "GREAT","magnificent", "magical",
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

    # bot.locations()

    while True:

        mode = 0

        if mode == 0:
            bot.auto_mod()
