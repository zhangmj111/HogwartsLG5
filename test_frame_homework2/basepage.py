import yaml
from appium.webdriver.webdriver import WebDriver

from test_frame_homework2.black_handles import black_handles


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_handles
    def find(self, locator):
        return self.driver.find_element(*locator)

    @black_handles
    def find_and_click(self, locator):
        self.find(locator).click()

    @black_handles
    def find_and_sendkeys(self, locator, text):
        self.find(locator).send_keys(text)

    @black_handles
    def find_and_gettext(self, locator):
        return self.find(locator).text

    def run_steps(self, page_path, operation):
        with open(page_path, 'r', encoding='utf-8') as f:
            datas = yaml.safe_load(f)[operation]
            for data in datas:
                if 'find_and_click' == data['action']:
                    self.find_and_click(data['locator'])
                elif 'find_and_sendkeys' == data['action']:
                    self.find_and_sendkeys(data['locator'], data['context'])
                elif 'find_and_gettext' == data['action']:
                    self.find_and_gettext(data['locator'])
