from pages.base_page import BasePage
from components.components import WebElement

class AlertsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)


        self.btn_alert = WebElement(driver, '#alertButton')
        self.btn_confirm = WebElement(driver, '#confirmButton')
        self.confirmResult = WebElement(driver, '#confirmResult')
        self.btn_prompt = WebElement(driver, '#promtButton')
        self.promptResult = WebElement(driver, '#promptResult')
        self.btn_alert_5 = WebElement(driver, '#timerAlertButton')