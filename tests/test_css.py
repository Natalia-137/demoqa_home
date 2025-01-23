from pages.textbox_page import TextboxPage
from components.components import WebElement

def test_text_box_submit(browser):
    textbox_page = TextboxPage(browser)

    textbox_page.visit()
    assert textbox_page.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert textbox_page.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert textbox_page.btn_submit.check_css('borderColor', 'rgb(0, 123, 255)')