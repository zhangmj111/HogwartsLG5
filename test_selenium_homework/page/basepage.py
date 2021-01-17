import json

from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self._cookie_login()
        else:
            self.driver = base_driver

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("D:/cookie.json") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        self.find(locator).send_keys(value)