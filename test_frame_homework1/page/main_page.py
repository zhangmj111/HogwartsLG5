from appium.webdriver.common.mobileby import MobileBy

from test_frame_homework1.basepage import BasePage
from test_frame_homework1.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.find_and_click((MobileBy.ID, "com.xueqiu.android:id/post_status"))
        self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)
