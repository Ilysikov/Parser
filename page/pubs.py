from selenium.webdriver.common.by import By

from page.create_rub import CreateRub


class PageRub(CreateRub):

    def all_pages(self):
        try:
            all = self.driver.find_elements(By.XPATH,
                                            '//*[@id = "pager"]/li/a')
        except:
            all = []

        return [{'name': r.text, 'href': r.get_attribute('href')} for r in all] if all else []

    def all_pubs(self):
        all = self.driver.find_elements(By.XPATH,
                                        '//*[@class = "public_li"]/li/a')

        return [{'name': r.text, 'href': r.get_attribute('href')} for r in all]
