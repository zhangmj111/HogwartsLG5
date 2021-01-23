from appium.webdriver.common.mobileby import MobileBy

from test_frame_homework2.basepage import BasePage
from test_frame_homework2.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps('../page/market_page.yaml', 'goto_search')
        return SearchPage(self.driver)