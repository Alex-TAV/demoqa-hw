import time
from pages.accordion import Accordion

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.text_lorem_ipsum.visible()
    accordion_page.btn_lorem_ipsum.click()
    time.sleep(2)
    assert not accordion_page.text_lorem_ipsum.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.text_where_does_it_come_from_1.visible()
    assert not accordion_page.text_where_does_it_come_from_2.visible()
    assert not accordion_page.text_why_do_we_use_it.visible()