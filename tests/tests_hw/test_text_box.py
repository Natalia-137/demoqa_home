from pages.textbox_page import TextboxPage
from components.components import WebElement

def test_text_box(browser):
    texbox_page = TextboxPage(browser)

    texbox_page.visit()
    texbox_page.textbox_1.send_keys('Ararat')
    texbox_page.current_adress.send_keys('Addis-Abbeba')
    texbox_page.btn_submit.click_force()

    assert texbox_page.down_place_name.get_text() == 'Name:Ararat'
    assert texbox_page.down_place_current_adress.get_text() == 'Current Address :Addis-Abbeba'






