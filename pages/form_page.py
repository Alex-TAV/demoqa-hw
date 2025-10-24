from componeents.componeents import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.hobbies_checkbox_1 = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.user_form = WebElement(driver, '#userForm')
        self.select_state = WebElement(driver, '#react-select-3-input')
        self.select_state_check = WebElement(driver, '#state > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')
        self.select_city = WebElement(driver, '#react-select-4-input')
        self.select_city_check = WebElement(driver, '#city > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')

