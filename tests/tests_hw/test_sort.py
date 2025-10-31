from pages.webtables_page import WebTablesPage
import time


def test_webtables(browser):
    webtables_page = WebTablesPage(browser)

    webtables_page.visit()

    webtables_page.column_first_name_btn.click()
    assert webtables_page.column_first_name_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    webtables_page.column_first_name_btn.click()
    assert webtables_page.column_first_name_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    webtables_page.column_last_name_btn.click()
    assert webtables_page.column_last_name_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    webtables_page.column_last_name_btn.click()
    assert webtables_page.column_last_name_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    webtables_page.column_age_btn.click()
    assert webtables_page.column_age_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    webtables_page.column_age_btn.click()
    assert webtables_page.column_age_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    webtables_page.column_email_btn.click()
    assert webtables_page.column_email_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    webtables_page.column_email_btn.click()
    assert webtables_page.column_email_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    webtables_page.column_salary_btn.click()
    assert webtables_page.column_salary_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    webtables_page.column_salary_btn.click()
    assert webtables_page.column_salary_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    webtables_page.column_department_btn.click()
    assert webtables_page.column_department_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    webtables_page.column_department_btn.click()
    assert webtables_page.column_department_btn.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
