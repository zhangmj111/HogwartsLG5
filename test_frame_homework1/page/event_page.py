from appium.webdriver.common.mobileby import MobileBy

from test_frame_homework1.basepage import BasePage


class EventPage(BasePage):
    def get_event_title(self):
        result = self.find_and_gettext((MobileBy.ID, "com.xueqiu.android:id/action_title"))
        return result