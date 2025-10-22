import time
from pages.elements_page import ElementsPage


# # По этому тесту проверка должна выдавать ошибку
# def test_visible_btn_sidebar_1(browser):
#     elements_page = ElementsPage(browser)
#     elements_page.visit()
#     # elements_page.btn_sidebar_first.click()
#     # time.sleep(3)
#     # assert elements_page.btn_sidebar_first_textbox.exist()

# Исправляем ошибку из пред идущего теста
def test_visible_btn_sidebar_2(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_textbox.visible()

# Проверка, что элемент не виден
def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.visible()