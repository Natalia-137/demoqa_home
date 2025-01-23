from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_menu = WebElement (driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')

        self.btn_small_dialog = WebElement(driver, '#showSmallModal')
        self.btn_large_dialog = WebElement(driver, '#showLargeModal')
        self.close_small_dialog = WebElement(driver, '#closeSmallModal')
        self.close_large_dialog = WebElement(driver, '#closeLargeModal')
        self.small_dialog_window = WebElement(driver, "body > div.fade.modal.show > div")
        self.large_dialog_window = WebElement(driver, "modal-dialog modal-lg", 'class')
