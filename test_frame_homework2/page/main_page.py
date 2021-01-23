from appium.webdriver.common.mobileby import MobileBy

from test_frame_homework2.basepage import BasePage
from test_frame_homework2.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.run_steps("../page/main_page.yaml", 'goto_market')
        return MarketPage(self.driver)
