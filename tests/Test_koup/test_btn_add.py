from pages.koup import KoupPage
from pages.koup_add_page import KoupAddPage
from components.components import WebElement
import time

def test_btn_add(browser):
    page_koup = KoupPage(browser)
    page_koup_add = KoupAddPage(browser)

    page_koup.visit()
    assert page_koup.link_add.get_text() == 'Add/Remove Elements'
    page_koup.link_add.click()
    # time.sleep(2)
    # assert page_koup_add.equal_url()
    assert page_koup_add.btn_add.get_text() == 'Add Element'
    assert page_koup_add.btn_add.get_dom_attribute(name='onclick') == 'addElement()'

    for i in range(4):
        page_koup_add.btn_add.click()

    # assert page_koup_add.btn_del.check_count_elements(4)

    for j in range(4):
        page_koup_add.btn_del.click()

    time.sleep(2)

    assert not page_koup_add.btn_del.exist()

