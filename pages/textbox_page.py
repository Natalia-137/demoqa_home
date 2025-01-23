from pages.base_page import BasePage
from components.components import WebElement

class TextboxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.textbox_1 = WebElement(driver, '#userName','css')
        self.current_adress = WebElement(driver, '#currentAddress', 'css')
        self.btn_submit = WebElement(driver, '#submit', 'css')
        self.down_place_name = WebElement(driver, 'mb-1', 'class')
        self.down_place_current_adress = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[2]', 'xpath')
