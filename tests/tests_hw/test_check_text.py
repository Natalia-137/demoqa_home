from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


# def test_text_in_footer(browser):
#
#     demo_qa_page = DemoQa (browser)
#     demo_qa_page.visit()


def test_page_elements (browser):
    el_page = ElementsPage (browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()

