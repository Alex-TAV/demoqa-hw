from pages.text_box_page import TextBoxPage
import time

def test_text_box_page(browser):
    text_box_page = TextBoxPage(browser)

    name = 'Tester'
    address = 'Test Address'

    text_box_page.visit()
    text_box_page.full_name.send_keys(name)
    text_box_page.current_address.send_keys(address)
    time.sleep(2)
    text_box_page.btn_submit.click()
    time.sleep(2)
    assert text_box_page.full_name_check.get_text() ==  f'Name:{name}'
    assert text_box_page.current_address_check.get_text() == f'Current Address :{address}'
