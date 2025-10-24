from pages.text_box_page import TextBoxPage
import time

def test_clear(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('Tester')
    time.sleep(2)
    assert text_box_page.full_name.get_attribute() == 'Tester' # get_attribute() - получает значение указанного атрибута HTML-элемента
    text_box_page.full_name.clear()
    time.sleep(2)
    assert text_box_page.full_name.get_text() == '' # get_text() - получает видимый текст, заключённый внутри HTML-элемента

