from selenium.webdriver.common.by import By


class CreateRub:

    def __init__(self, driver, wait=None):
        self.driver = driver
        self.wait = wait

    def all_rub(self):
        all = self.driver.find_elements(By.XPATH,
                                        '//*[@class = "menu_right"]/div/ul/li/a')

        return [{'name': r.text, 'href': r.get_attribute('href')} for r in all]
