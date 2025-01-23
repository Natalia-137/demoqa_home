from pages.modal_dialogs import ModalDialogs
from pages.alerts_page import AlertsPage
from components.components import WebElement
import time

def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    assert modal_page.btn_small_dialog.exist()
    assert modal_page.btn_large_dialog.exist()

    modal_page.btn_small_dialog.click()
    time.sleep(2)
    assert modal_page.small_dialog_window.exist()
    modal_page.close_small_dialog.click()
    time.sleep(2)
    assert not modal_page.small_dialog_window.exist()

    modal_page.btn_large_dialog.click()
    time.sleep(2)
    assert modal_page.small_dialog_window.exist()
    modal_page.close_large_dialog.click()
    assert not modal_page.small_dialog_window.exist()





