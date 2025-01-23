from pages.webtables_page import WebTablePage
from components.components import WebElement
import time

def test_webtables(browser):
    webtable_page = WebTablePage(browser)

    webtable_page.visit()
    assert not webtable_page.block_no_rows.exist()
    while webtable_page.btn_del.exist():
        webtable_page.btn_del.click()

    time.sleep(3)
    assert webtable_page.block_no_rows.exist()
