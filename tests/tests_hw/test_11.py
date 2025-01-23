from pages.webtables_page import WebTablePage
from components.components import WebElement
import time

def test_dialig_form(browser):
    table_page = WebTablePage(browser)

    table_page.visit()
    assert not table_page.modal_win.exist()
    table_page.btn_add.get_text() == 'Add'
    table_page.btn_add.click()
    assert table_page.modal_win.exist()

    table_page.modal_btn_submit.click()
    table_page.modal_btn_submit.get_dom_attribute(name='class') == 'was-validated'

    table_page.modal_first_name.send_keys('qwe')
    table_page.modal_last_name.send_keys('asd')
    table_page.modal_email.send_keys('wer@tr.tt')
    table_page.modal_age.send_keys('23')
    table_page.modal_salary.send_keys('2000')
    table_page.modal_dep.send_keys('tytyty')

    table_page.modal_btn_submit.click()
    time.sleep(2)
    assert not table_page.modal_win.exist()

    assert table_page.table_first_name.get_text() == 'qwe'
    assert table_page.table_last_name.get_text() == 'asd'
    assert table_page.table_age.get_text() == '23'
    assert table_page.table_email.get_text() == 'wer@tr.tt'
    assert table_page.table_salary.get_text() == '2000'
    assert table_page.table_dep.get_text() == 'tytyty'

    table_page.table_redact.click()
    assert table_page.modal_win.exist()

    table_page.modal_first_name.clear()
    table_page.modal_first_name.send_keys('poiuy')
    table_page.modal_btn_submit.click()
    time.sleep(2)
    assert table_page.table_first_name.get_text() == 'poiuy'

    table_page.table_delete.click()
    assert table_page.table_first_name.get_text() == ' '
    assert table_page.table_last_name.get_text() == ' '
    assert table_page.table_age.get_text() == ' '
    assert table_page.table_email.get_text() == ' '
    assert table_page.table_salary.get_text() == ' '
    assert table_page.table_dep.get_text() == ' '
    assert not table_page.table_redact.exist()
    assert not table_page.table_delete.exist()

