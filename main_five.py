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
        with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic['name']}/file.html', 'r') as r:
            soup = BeautifulSoup(r, 'lxml')
            parent = soup.find('div', class_='text_content')
            with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic["name"]}/soup.html',
                      'w', encoding='utf-8') as f:
                f.write(parent.prettify())
