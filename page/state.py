from selenium.webdriver.common.by import By


class StateImage:

    def __init__(self, driver, wait=None, name=None):
        self.driver = driver
        self.wait = wait
        self.name = name

    def link_image(self):
        all = self.driver.find_elements(By.XPATH, '//*[@class="content"]//img')

        return {'name': self.name, 'href': [r.get_attribute('src') for r in all]}



