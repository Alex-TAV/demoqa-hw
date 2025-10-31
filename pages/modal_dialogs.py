from componeents.componeents import WebElement
from pages.base_page import BasePage

class ModalDialog(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_first_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal')