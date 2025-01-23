from pages.form_page import FormPage
from components.components import WebElement

def test_login_form_validate(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute(name='placeholder')
    assert form_page.last_name.get_dom_attribute(name='placeholder')
    assert form_page.user_email.get_dom_attribute(name='placeholder')
    assert form_page.user_email.get_dom_attribute(name='pattern')
    form_page.btn_submit.click_force()
    assert form_page.full_form.get_dom_attribute(name='class') == 'was-validated'





