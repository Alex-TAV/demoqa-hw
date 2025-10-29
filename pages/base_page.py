from selenium.webdriver.common.by import By
import logging


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)


    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False

# Метод back переходить обратно на страницу (стрелочка назад)
    def back(self):
        self.driver.back()

# Метод forward переходить обратно на страницу (стрелочка вперёд)
    def forward(self):
        self.driver.forward()

# Метод refresh обновление страницы
    def refresh(self):
        self.driver.refresh()

# Метод get_title взять заголовок
    def get_title(self):
        return self.driver.title

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False