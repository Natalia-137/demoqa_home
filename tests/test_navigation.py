from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demoqa = DemoQa(browser)
    el_page = ElementsPage(browser)

    demoqa.visit()
    demoqa.btn_elements.click()

    demoqa.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert el_page.equal_url()