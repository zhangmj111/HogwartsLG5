from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework2.page.add_contact_page import AddContactPage
from test_appium_homework2.page.basepage import BasePage


class AddContactAddressPage(BasePage):
    def goto_add_contact(self):
        locator = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
        self.find_and_click(locator)
        return AddContactPage(self.driver)

    def get_toast(self):
        locator2 = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        res = self.find_and_gettext(locator2)
        return res
