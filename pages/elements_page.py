from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from componeents.componeents import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_is_centered = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
