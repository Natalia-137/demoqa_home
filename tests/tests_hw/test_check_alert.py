from pages.alerts_page import AlertsPage
import time

def test_check_alert_5min(browser):
    alert_page = AlertsPage(browser)
    alert_page.visit()

    assert not alert_page.alert()

    # assert alert_page.btn_alert_5.exist()
    alert_page.btn_alert_5.click()
    time.sleep(7)
    # assert alert_page.alert()
    # alert_page.alert().accept()
    # time.sleep(7)
    # assert not alert_page.alert()