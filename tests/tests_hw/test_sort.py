from pages.webtables_page import WebTablePage
import time

def test_sort(browser):
    table_page = WebTablePage(browser)

    table_page.visit()
    table_page.name_first_name.click()
    time.sleep(5)

    # assert table_page.row.