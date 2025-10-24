from pages.form_page import FormPage
import time

def test_login_form_validate(browser):
    from_page = FormPage(browser)

    from_page.visit()
    assert from_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert from_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert from_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert from_page.user_email.get_dom_attribute('pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$' # raw-строка (r'') используется чтобы все обратные слэши интерпретировались как обычные символы!
    from_page.btn_submit.click_force()
    time.sleep(2)
    assert from_page.user_form.get_dom_attribute('class') == 'was-validated'
