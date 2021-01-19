from appium.webdriver.common.mobileby import MobileBy

from test_frame_homework1.basepage import BasePage
from test_frame_homework1.page.event_page import EventPage


class MarketPage(BasePage):
    def goto_event(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='立即登录']"))
        self.find_and_click((MobileBy.ID, "com.xueqiu.android:id/enter_uncommon_event"))
        return EventPage(self.driver)