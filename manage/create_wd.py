from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class CreateWd:

    def __init__(self, url='http://www.pravsemia.ru/articles/center.htm'):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = url
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 20)

    def wait(self):
        return self.wait

    def gets(self, url):
        self.url = url
        self.driver.get(str(self.url))
        return self.driver
