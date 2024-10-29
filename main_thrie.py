import json
import os

import pdfkit
import requests

from manage.create_wd import CreateWd
from page.state import StateImage
from bs4 import BeautifulSoup

rubs = json.load(open('/Users/ivanlysikov/PycharmProjects/CSM/catalog/list_rubs.json'))
for rub in rubs:
    for dic in rub['state']:
            with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic['name']}/page.html', 'r') as r:
                soup = BeautifulSoup(r, 'html.parser')
                parent = soup.find('div', class_='content')
                images = parent.findAll('img')
                if not images:
                    continue
                for c, img in enumerate(images):
                    try:
                        jpg=requests.get(f"http://www.pravsemia.ru{img.get('src')}")
                        os.makedirs(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic["name"]}/photo/', exist_ok=True)
                        with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic["name"]}/photo/{c+1}.jpg',
                                'wb') as f:
                            f.write(jpg.content)
                    except:
                        continue


            # wd = CreateWd(url=dic['href'])
            # page_state = StateImage(wd, dic['name'])
            # list_image = page_state.link_image()
            # for image in list_image:
            #     jpg = requests.get(image['href'])
            #     with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic["name"]}/photo/{image['href'][:-4]}.jpg',
            #               'wb') as f:
            #         f.write(jpg.content)
