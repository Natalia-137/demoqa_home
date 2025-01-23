from pages.base_page import BasePage
from components.components import WebElement

class WebTablePage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody')
        self.block_no_rows = WebElement(driver, 'div.rt-noData')
        self.btn_del = WebElement(driver, '//*[@id="delete-record-*"]/svg/path', 'xpath')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_win = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.modal_btn_submit = WebElement (driver, '#submit')
        self.modal_first_name = WebElement(driver, '#firstName')
        self.modal_last_name = WebElement(driver, '#lastName')
        self.modal_email = WebElement(driver, '#userEmail')
        self.modal_age = WebElement(driver, '#age')
        self.modal_salary = WebElement(driver, '#salary')
        self.modal_dep = WebElement(driver, '#department')
        self.table_first_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.table_last_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.table_email = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.table_age = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)')
        self.table_salary = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)')
        self.table_dep = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')
        self.table_redact = WebElement(driver, '#edit-record-4')
        self.table_delete = WebElement(driver, '#delete-record-4')

        self.name_first_name = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath')
        self.row = WebElement(driver, 'rt-tr-group', 'class')
