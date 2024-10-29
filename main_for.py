import json
from bs4 import BeautifulSoup

rubs = json.load(open('/Users/ivanlysikov/PycharmProjects/CSM/catalog/list_rubs.json'))
for rub in rubs:
    for dic in rub['state']:
            with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic['name']}/page.html', 'r') as r:
                soup = BeautifulSoup(r, 'html.parser')
                parent = soup.find('div', class_='content')
                text = parent.text
                with open(f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub["name"]}/{dic["name"]}/doc.txt',
                        'w', encoding='utf-8') as f:
                            f.write(text)
