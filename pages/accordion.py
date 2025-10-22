from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from componeents.componeents import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian/'
        super().__init__(driver, self.base_url)

        self.text_lorem_ipsum = WebElement(driver, '#section1Content > p')
        self.btn_lorem_ipsum = WebElement(driver, '#section1Heading')
        self.text_where_does_it_come_from_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.text_where_does_it_come_from_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.text_why_do_we_use_it = WebElement(driver, '#section3Content > p')