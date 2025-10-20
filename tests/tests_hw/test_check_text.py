# Создайте директорию tests_hw в папке tests все домашние тесты создавайте в ней
# 2. в файле test_check_text.py реализуйте таст кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
# 3. в файле test_check_text.py реализуйте таст кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. через кнопку перейти на страницу 'https://demoqa.com/elements'
# c. проверить что текст по центру == 'Please select an item from left to start practice.'
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text_in_footer(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.text_in_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_in_centered(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
    assert elements_page.text_is_centered.get_text() == 'Please select an item from left to start practice.'
