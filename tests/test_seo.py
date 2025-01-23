import time

from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts_page import AlertsPage
from pages.browser_tab import BrowserTab
import pytest

# def test_check_title_demo (browser):
#     page_demoqa = DemoQa(browser)
#
#     page_demoqa.visit()
#     assert browser.title == 'DEMOQA'

@pytest.mark.parametrize('pages', [Accordion, AlertsPage, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert browser.title == 'DEMOQA'