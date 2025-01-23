from conftest import browser
from pages.textbox_page import TextboxPage
from components.components import WebElement
import time

def test_clear(browser):
    textbox_page = TextboxPage(browser)

    textbox_page.visit()
    textbox_page.textbox_1.send_keys(text='Ararat')
    time.sleep(2)
    textbox_page.textbox_1.clear()
    time.sleep(2)
    assert textbox_page.textbox_1.get_text() == ''
