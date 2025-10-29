from pages.webtables_page import WebTablesPage
from selenium.webdriver.common.keys import Keys
import time


def test_webtables(browser):
    webtables_page = WebTablesPage(browser)

    webtables_page.visit()

    # Проверка отсутствия блока No rows found
    assert not webtables_page.no_rows_found.exist()

    # Удаление записей из таблицы
    while webtables_page.btns_delete.exist():
        webtables_page.btns_delete.click()

    # Проверка открытия блока No rows found
    time.sleep(2)
    assert webtables_page.no_rows_found.exist()


def test_add_and_change_a_line(browser):
    webtables_page = WebTablesPage(browser)

    # Исходные данные для теста
    fn_1 = 'John'; fn_2 = 'Jim'
    ln_1 = 'Doe'
    email_1 = 'JD@jjj.dd'
    age_1 = 10
    sal_1 = 1000
    dep_1 = 'Department'

    webtables_page.visit()
    webtables_page.btn_add.click()
    time.sleep(2)

    webtables_page.first_name.send_keys(fn_1)
    webtables_page.last_name.send_keys(ln_1)
    webtables_page.email.send_keys(email_1)
    webtables_page.age.send_keys(age_1)
    webtables_page.salary.send_keys(sal_1)
    webtables_page.department.send_keys(dep_1)
    webtables_page.btn_submit.click()
    time.sleep(2)
    assert webtables_page.check_first_name_4.get_text() == fn_1

    webtables_page.btn_edit_4.click()
    time.sleep(2)
    webtables_page.first_name.clear()
    webtables_page.first_name.send_keys(fn_2)
    webtables_page.btn_submit.click()
    time.sleep(2)
    assert webtables_page.check_first_name_4.get_text() == fn_2

    webtables_page.btn_delete_4.click()
    time.sleep(2)
    assert webtables_page.check_first_name_4.get_text() == ' '

def test_check_the_buttons(browser):
    webtables_page = WebTablesPage(browser)

    # Исходные данные для теста
    fn_1 = 'Tester'; fn_2 = 'Jim'; fn_3 = 'John'
    ln_1 = 'Testerovich'; ln_2 = 'John'; ln_3 = 'Doe'
    email_1 = 'test@test.tt'; email_2 = 'JJJ@jjj.jj'; email_3 = 'JD@jjj.dd'
    age_1 = 30; age_2 = 20; age_3 = 33
    sal_1 = 4000; sal_2 = 1000; sal_3 = 3500
    dep_1 = 'Department_1'; dep_2 = 'Department_2'; dep_3 = 'Department_3'

    webtables_page.visit()
    webtables_page.btn_rows.click()
    webtables_page.btn_rows.send_keys(Keys.PAGE_UP)
    webtables_page.btn_rows.send_keys(Keys.ENTER)
    time.sleep(2)

    # Проверка, что кнопки имеют аргумент 'disabled'
    assert webtables_page.btn_next.get_dom_attribute('disabled')
    assert webtables_page.btn_prev.get_dom_attribute('disabled')

    # Добавление в таблицу запись 1
    webtables_page.btn_add.click()
    time.sleep(2)
    webtables_page.first_name.send_keys(fn_1)
    webtables_page.last_name.send_keys(ln_1)
    webtables_page.email.send_keys(email_1)
    webtables_page.age.send_keys(age_1)
    webtables_page.salary.send_keys(sal_1)
    webtables_page.department.send_keys(dep_1)
    webtables_page.btn_submit.click()
    time.sleep(2)

    # Добавление в таблицу запись 2
    webtables_page.btn_add.click()
    time.sleep(2)
    webtables_page.first_name.send_keys(fn_2)
    webtables_page.last_name.send_keys(ln_2)
    webtables_page.email.send_keys(email_2)
    webtables_page.age.send_keys(age_2)
    webtables_page.salary.send_keys(sal_2)
    webtables_page.department.send_keys(dep_2)
    webtables_page.btn_submit.click()
    time.sleep(2)

    # Добавление в таблицу запись 3
    webtables_page.btn_add.click()
    time.sleep(2)
    webtables_page.first_name.send_keys(fn_3)
    webtables_page.last_name.send_keys(ln_3)
    webtables_page.email.send_keys(email_3)
    webtables_page.age.send_keys(age_3)
    webtables_page.salary.send_keys(sal_3)
    webtables_page.department.send_keys(dep_3)
    webtables_page.btn_submit.click()
    time.sleep(2)

    # Проверка, что кнопка Next имеют аргумент 'disabled' (НЕ заблокирована)
    assert not webtables_page.btn_next.get_dom_attribute('disabled')
    webtables_page.btn_next.click()
    time.sleep(2)

    # Проверка, что открылась страница 2 таблицы
    assert webtables_page.page_number.get_dom_attribute('value') == '2'

    # Проверка, что кнопка Previous имеют аргумент 'disabled' (НЕ заблокирована)
    assert not webtables_page.btn_prev.get_dom_attribute('disabled')
    webtables_page.btn_prev.click()
    time.sleep(2)

    # Проверка, что открылась страница 1 таблицы
    assert webtables_page.page_number.get_dom_attribute('value') == '1'