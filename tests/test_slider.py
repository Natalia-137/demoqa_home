from pages.slider_page import SliderPage
from selenium.webdriver.common.keys import Keys
import time

def test_slider(browser):
    slider_page = SliderPage(browser)

    slider_page.visit()
    slider_page.indicator.get_text() == '25'
    slider_page.slider.get_dom_attribute('value') == '25'

    while not slider_page.slider.get_dom_attribute('value') == '50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider.get_dom_attribute('value') == '50'
    assert slider_page.indicator.get_dom_attribute('value') == '50'