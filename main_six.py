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
            parent = soup.find('div', class_='content')
            doctype = '''
                    <!doctype html>
                    <html lang="ru">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport"
                                content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                            <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>Document</title>
                    </head>
                    <body>'''
            docend = '</body></html>'
            with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic["name"]}/page.html',
                      'w', encoding='utf-8') as f:
                f.write(doctype + parent.prettify() + docend)
