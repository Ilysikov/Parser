from page.create_rub import CreateRub


class Rubs:
    def __init__(self, wd):
        self.driver = wd.driver
        self.rubs_page = CreateRub(self.driver)
        self.list_rubs = ([{'href': 'http://www.pravsemia.ru/articles/center.htm', 'name': 'Жизнь нашего центра'}]
                          + self.rubs_page.all_rub())

    def all_rubs(self):
        return self.list_rubs
