from pages.base_page import BasePage
from pages.accordion import Accordion
from pages.alerts_page import AlertsPage
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab
from components.components import WebElement
import time
import pytest

@pytest.mark.parametrize('pages', [Accordion, AlertsPage])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    # assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'