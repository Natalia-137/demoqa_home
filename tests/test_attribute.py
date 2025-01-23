from pages.textbox_page import TextboxPage
from components.components import WebElement

def test_placeholder(browser):
    textbox_page = TextboxPage(browser)

    textbox_page.visit()
    assert textbox_page.textbox_1.get_dom_attribute(name='placeholder') == 'Full Name'