from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.el1 = WebElement (driver, '#section1Content > p')
        self.el2 = WebElement (driver, '#section1Heading')
        self.el3 = WebElement (driver, '#section2Content > p:nth-child(1)')
        self.el4 = WebElement (driver, '#section2Content > p:nth-child(2)')
        self.el5 = WebElement (driver, '#section3Content > p')