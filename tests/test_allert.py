from pages.alerts_page import AlertsPage
import time
from components.components import WebElement


def test_allert(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert.click()
    alert_page.alert().accept()
    time.sleep(7)
    assert alert_page.alert()

# def test_alert_text(browser):
#     alert_page = AlertsPage(browser)
#
#     alert_page.visit()
#     alert_page.btn_alert.click()
#     alert_page.alert().accept()
#     assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().accept()
    assert not alert_page.alert()

# def test_confirm(browser):
#     alert_page = AlertsPage(browser)
#
#     alert_page.visit()
#     alert_page.btn_confirm.click_force()
#     time.sleep(4)
#     assert alert_page.alert()
#     alert_page.alert().dismiss()
#     time.sleep(2)
#     assert alert_page.confirmResult.get_text() == 'You selected Cancel'

# def test_prompt(browser):
#     alert_page = AlertsPage(browser)
#
#     alert_page.visit()
#     alert_page.btn_prompt.click()
#     time.sleep(2)
#     alert_page.alert().send_keys('Asd')
#     alert_page.alert().accept()
#     time.sleep(2)
#     assert alert_page.promptResult.get_text() == 'You entered Asd'

