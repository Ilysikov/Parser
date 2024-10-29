import os

from page.pubs import PageRub


class Pubs:
    def __init__(self, wd, rub, rub_name):
        self.directory = f'/Users/ivanlysikov/PycharmProjects/CSM/catalog/{rub_name}'
        os.makedirs(self.directory, exist_ok=True)
        self.list_pub = []
        self.wd = wd
        self.driver = self.wd.gets(rub)
        self.page = PageRub(self.driver)
        self.rub_check = set()
        self.list_page = set()

    def append_pub(self):
        list_link = self.page.all_pubs()
        for s in list_link:
            if s not in self.list_pub:
                self.list_pub.append(s)

    def append_rub_list(self):
        list_page = self.page.all_pages()
        if list_page:
            for p in self.page.all_pages():
                if p['href'] not in self.list_page and p['href'] not in self.rub_check:
                    self.list_page.add(p['href'])

    def create_list_state(self):
        self.append_rub_list()
        self.append_pub()
        self.rub_check.add(self.wd.url)
        for rub in self.list_page:
            self.wd.gets(rub)
            self.page = PageRub(self.driver)
            self.append_pub()
            self.rub_check.add(self.wd.url)
        return True if self.rub_check.issuperset(self.list_page) else self.create_list_state()

    def all_pubs(self):
        return self.list_pub

