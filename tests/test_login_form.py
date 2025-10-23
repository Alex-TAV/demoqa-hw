import time
from pages.form_page import FormPage

def test_login_form(browser):
    from_page = FormPage(browser)

    from_page.visit()
    assert not from_page.modal_dialog.exist()
    time.sleep(2)

    from_page.first_name.send_keys('tester')
    from_page.last_name.send_keys('testerovich')
    from_page.user_email.send_keys('test@ttt.tt')
    from_page.gender_radio_1.click()
    from_page.user_number.send_keys('9992223344')
    time.sleep(2)

    from_page.btn_submit.click()
    time.sleep(2)