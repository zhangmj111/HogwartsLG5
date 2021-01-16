from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework2.page.basepage import BasePage
from test_appium_homework2.page.list_contact_page import ListContactPage


class MainPage(BasePage):
    def goto_list_contact(self):
        locator = (MobileBy.XPATH, '//*[@text="通讯录"]')
        self.find_and_click(locator)
        return ListContactPage(self.driver)
