from componeents.componeents import WebElement
from pages.base_page import BasePage


class WebTablesPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        # Элементы ЭФ (экранной формы) "Web Tables"
        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.btns_delete = WebElement(driver, 'span[title="Delete"]')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.btn_prev = WebElement(driver, 'div.-previous > button')
        self.btn_rows = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_edit_4 = WebElement(driver, '#edit-record-4 > svg > path')
        self.btn_delete_4 = WebElement(driver, '#delete-record-4 > svg > path')
        self.check_first_name_4 = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.page_number = WebElement(driver, 'input[type=number]')

        # Столбцы таблицы
        self.column_first_name_btn = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(1)')
        self.column_last_name_btn = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(2)')
        self.column_age_btn = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(3)')
        self.column_email_btn = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(4)')
        self.column_salary_btn = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(5)')
        self.column_department_btn = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(6)')


        # Элементы ЭФ "Registration Form"
        self.first_name = WebElement(driver, 'input#firstName')
        self.last_name = WebElement(driver, 'input#lastName')
        self.email = WebElement(driver, 'input#userEmail')
        self.age = WebElement(driver, 'input#age')
        self.salary = WebElement(driver, 'input#salary')
        self.department = WebElement(driver, 'input#department')
        self.btn_submit = WebElement(driver, 'button#submit')
