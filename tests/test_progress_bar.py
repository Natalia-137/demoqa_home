from pages.progress_bar import ProgressBar
import time

def test_progress_bar(browser):
    progress_page = ProgressBar(browser)
    progress_page.visit()

    assert progress_page.bar.get_dom_attribute('aria-valuenow') < '51'

    progress_page.btn_start.click()
    while True:
        if progress_page.bar.get_dom_attribute('aria-valuenow') == '50':
            progress_page.btn_start.click()
            break

    time.sleep(7)

    assert progress_page.bar.get_dom_attribute('aria-valuenow') == '51'