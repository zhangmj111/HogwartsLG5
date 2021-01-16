from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        self.find(locator).send_keys(text)

    def find_and_gettext(self, locator):
        return self.find(locator).text
