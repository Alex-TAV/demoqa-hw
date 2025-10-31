from pages.browser_tab import BrowserTab
from pages.links_page import LinksPage
from pages.demoqa import DemoQa
import time


def test_link_home(browser):
    links_page = LinksPage(browser)
    demo_qa_page = DemoQa(browser)

    links_page.visit()
    assert links_page.link_home.get_text() == 'Home'
    assert links_page.link_home.get_dom_attribute('href') == 'https://demoqa.com/'

    assert len(browser.window_handles) == 1
    links_page.link_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    assert demo_qa_page.equal_url()