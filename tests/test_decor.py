import pytest

from pages.demoqa import DemoQa
from pages.radio_btn_page import RadioPage
from components.components import WebElement
import time

@pytest.mark.skip
def test_decor(browser):
    demoqa_page = DemoQa(browser)
    demoqa_page.visit()

    # assert demoqa_page.menu.check_count_elements(6)
    assert demoqa_page.h5.check_count_elements(6)

    for element in demoqa_page.h5.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason='просто пропуск')
def test_radio_btn(browser):
    radio_page = RadioPage(browser)
    radio_page.visit()

    assert radio_page.yes_btn.exist()
    assert radio_page.impressiv_btn.exist()
    assert radio_page.no_btn.exist()
    assert not radio_page.text.exist()

    radio_page.yes_btn.click_force()
    time.sleep(2)
    assert radio_page.text.get_text() == 'You have selected Yes'

    radio_page.impressiv_btn.click_force()
    time.sleep(2)
    assert radio_page.text.get_text() == 'You have selected Impressive'

    assert radio_page.no_btn.get_dom_attribute('class') == 'custom-control-input disabled'
