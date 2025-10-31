import time
import pytest
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
from pages.alerts_page import AlertsPage
from pages.demoqa import DemoQa


@pytest.mark.parametrize('pages', [Accordion, AlertsPage, DemoQa, BrowserTab])
def test_check_teg_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'