import time
import pytest
from pages.modal_dialogs import ModalDialog


def test_check_2_button_modal(browser):
    modal_dialog_page = ModalDialog(browser)
    try:
        modal_dialog_page.visit()
        text_btn_sm = modal_dialog_page.btn_small_modal.get_text()
        if 'Small modal' not in text_btn_sm:
            pytest.skip('Страница недоступна, тестовый элемент не загружен')
    except Exception:
        pytest.skip('Страница недоступна, проблема с сетью')

# Для отображения причины пропуска теста, требуется запускать тест командой:
# pytest -ra tests/tests_hw/test_check_modal.py

    assert modal_dialog_page.btn_small_modal.exist()
    modal_dialog_page.btn_small_modal.click()
    time.sleep(2)
    modal_dialog_page.btn_close_small_modal.click()

    assert modal_dialog_page.btn_large_modal.exist()
    modal_dialog_page.btn_large_modal.click()
    time.sleep(2)
    modal_dialog_page.btn_close_large_modal.click()
