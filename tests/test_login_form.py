import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    from_page = FormPage(browser)

    from_page.visit()
    assert not from_page.modal_dialog.exist()
    time.sleep(2)

    from_page.first_name.send_keys('tester')
    from_page.last_name.send_keys('testerovich')
    from_page.user_email.send_keys('test@ttt.tt')
    from_page.gender_radio_1.click_force() # Без принудительного клика (click_force()) не нажимается
    from_page.user_number.send_keys('9992223344')
    from_page.hobbies_checkbox_1.click_force()
    from_page.current_address.send_keys('City Testeroso')
    time.sleep(2)

    from_page.btn_submit.click_force() # Можно использовать обычный метод click()
    time.sleep(2)
    assert from_page.modal_dialog.exist()
    from_page.btn_close_modal.click_force() # Можно использовать обычный метод click()


def test_login_form_hw(browser):
    from_page = FormPage(browser)
    name_state = 'NCR'
    name_city = 'Noida'

    from_page.visit()
    from_page.select_state.send_keys(name_state)
    time.sleep(2)
    from_page.select_state.enter()
    time.sleep(2)
    from_page.select_city.send_keys(name_city)
    time.sleep(2)
    from_page.select_city.enter()
    assert from_page.select_state_check.get_text() == name_state
    assert from_page.select_city_check.get_text() == name_city

def test_state_1(browser):
    from_page = FormPage(browser)

    from_page.visit()
    time.sleep(2)
    from_page.btn_state.scroll_to_element()
    from_page.btn_state.click()
    from_page.btn_NCR.click()
    time.sleep(2)

def test_state_2(browser):
    from_page = FormPage(browser)

    from_page.visit()
    time.sleep(2)
    from_page.btn_state.scroll_to_element()
    time.sleep(2)
    from_page.select_state.send_keys('NCR')
    from_page.select_state.send_keys(Keys.ENTER)
    time.sleep(2)

def test_state_3(browser):
    from_page = FormPage(browser)

    from_page.visit()
    time.sleep(2)
    from_page.btn_state.scroll_to_element()
    time.sleep(2)
    from_page.btn_state.click()
    from_page.select_state.send_keys(Keys.PAGE_DOWN)
    from_page.select_state.send_keys(Keys.ENTER)
    time.sleep(2)