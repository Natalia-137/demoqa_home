from pages import accordion
from pages.accordion import Accordion
import time


# def test_visit_page (browser):
#     page_accordion = Accordion(browser)
#
#     page_accordion.visit()
#     # assert page_accordion.el1.visible()
#
#     page_accordion.el2.click()
#     time.sleep(2)
#     assert not page_accordion.el1.visible()

def test_visible_accordion_default(browser):
    page_accordion = Accordion(browser)

    page_accordion.visit()
    assert not page_accordion.el3.visible()
    assert not page_accordion.el4.visible()
    assert not page_accordion.el5.visible()


