from pages.modal_dialogs import ModalDialog
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_dialog_page = ModalDialog(browser)

    modal_dialog_page.visit()
    assert modal_dialog_page.equal_url()
    assert modal_dialog_page.btns_first_menu.check_count_element(count=5)

def test_navigation_modal(browser):
    modal_dialog_page = ModalDialog(browser)
    demo_qa_page = DemoQa(browser)

    modal_dialog_page.visit()
    browser.refresh()
    modal_dialog_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)