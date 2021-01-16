from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework2.page.add_contact_address_page import AddContactAddressPage
from test_appium_homework2.page.basepage import BasePage


class ListContactPage(BasePage):
    def goto_add_contact_address(self):
        locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                                 '.scrollIntoView(new UiSelector().text("添加成员"))')
        self.find_and_click(locator)
        return AddContactAddressPage(self.driver)
