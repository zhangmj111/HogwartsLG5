from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework2.page.basepage import BasePage


class AddContactPage(BasePage):
    def edit_name(self, name):
        locator = (MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]')
        self.find_and_sendkeys(locator, f'{name}')
        return self

    def edit_gender(self, gender):
        locator = (MobileBy.XPATH, '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/aub"]')
        self.find_and_click(locator)
        locator1 = (MobileBy.XPATH, f'//*[@resource-id="com.tencent.wework:id/b9z"]//*[@text="{gender}"]')
        self.find_and_click(locator1)
        return self

    def edit_phone(self, phone):
        locator = (MobileBy.ID, 'com.tencent.wework:id/eq7')
        self.find_and_sendkeys(locator, f'{phone}')
        return self

    def edit_address(self, address):
        locator1 = (MobileBy.XPATH, '//*[@text="地址"]/..//*[@resource-id="com.tencent.wework:id/aub"]')
        self.find_and_click(locator1)
        locator2 = (MobileBy.ID, 'com.tencent.wework:id/gz')
        self.find_and_sendkeys(locator2, f'{address}')
        locator3 = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gur" and @text="确定"]')
        self.find_and_click(locator3)
        return self

    def save_contact(self):
        locator1 = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gur" and @text="保存"]')
        self.find_and_click(locator1)
        locator2 = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        res = self.find_and_gettext(locator2)
        return res
