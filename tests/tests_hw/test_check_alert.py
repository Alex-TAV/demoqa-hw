from pages.alerts_page import AlertsPage
import time

def test_alert_timer(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert_timer.click()
    time.sleep(6)
    assert alert_page.alert()