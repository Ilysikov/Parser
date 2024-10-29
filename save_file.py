import json
import os
import pdfkit
import requests
from bs4 import BeautifulSoup


class SaveFile:
    rubs = json.load(open('../CSM/catalog/list_rubs.json'))

    def createre_(self):
        for rub in self.rubs:
            for dic in rub['state']:
                patch = f'../CSM/catalog/{rub["name"]}/{dic["name"]}/'
                if not os.path.exists(patch):
                    self.create_dir(patch)
                self.worker(patch, dic)

    def worker(self, rub, dic):
        pass

    def create_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)


class SaveHtml(SaveFile):

    def worker(self, path, dic):
        self.create_html(path, dic)

    def create_html(self, path, dic):
        page_state = requests.get(dic['href'])
        with open(f'{path}file.html',
                  'w', encoding='utf-8') as h:
            h.write(page_state.text)


class SavePdf(SaveFile):
    def worker(self, path, dic):
        try:
            pdf = pdfkit.from_url(url=dic['href'])
            with open(
                    f'{path}pdf_file.pdf',
                    'wb') as f:
                f.write(pdf)
        except:
            pass


class SavePhoto(SaveHtml):

    def worker(self, path, dic):
        path_file = f'{path}file.html'
        if not os.path.isfile(path_file):
            self.create_html(path, dic)
        with open(path_file,
                  'r') as r:
            soup = BeautifulSoup(r, 'html.parser')
            parent = soup.find('div', class_='content')
            images = parent.findAll('img')
            if not images:
                return None
            for c, img in enumerate(images):
                try:
                    jpg = requests.get(f"http://www.pravsemia.ru{img.get('src')}")
                    os.makedirs(
                        f'{path}photo/',
                        exist_ok=True)
                    with open(
                            f'{path}photo/{c + 1}.jpg',
                            'wb') as f:
                        f.write(jpg.content)
                except:
                    continue


class SaveDoc(SaveHtml):
    def worker(self, path, dic):
        path_file = f'{path}file.html'
        if not os.path.isfile(path_file):
            self.create_html(path, dic)
        with open(path_file,
                  'r') as r:
            soup = BeautifulSoup(r, 'html.parser')
            parent = soup.find('div', class_='content')
            text = parent.text
            with open(f'{path}doc.txt',
                      'w', encoding='utf-8') as f:
                f.write(text)


class SavePageHtml(SaveHtml):
    def worker(self, path, dic):
        path_file = f'{path}file.html'
        if not os.path.isfile(path_file):
            self.create_html(path, dic)
        with open(path_file,
                  'r') as r:
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
            doc_end = '</body></html>'
            with open(f'{path}page.html',
                      'w', encoding='utf-8') as f:
                f.write(doctype + parent.prettify() + doc_end)


class SaveSoupText(SaveHtml):
    def worker(self, path, dic):
        path_file = f'{path}file.html'
        if not os.path.isfile(path_file):
            self.create_html(path, dic)
        with open(path_file,
                  'r') as r:
            soup = BeautifulSoup(r, 'lxml')
            parent = soup.find('div', class_='text_content')
            with open(f'{path}soup.html',
                      'w', encoding='utf-8') as f:
                f.write(parent.prettify())


class CallSave:
    nomen = {
        'html': SaveHtml,
        'pdf': SavePdf,
        'doc': SaveDoc,
        'photo': SavePhoto,
        'page': SavePageHtml,
        'soup': SaveSoupText,
    }

    def __init__(self, nomen):
        save = self.nomen[nomen]()
        save.createre_()
