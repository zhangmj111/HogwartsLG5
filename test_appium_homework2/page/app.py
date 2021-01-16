from appium import webdriver

from test_appium_homework2.page.basepage import BasePage
from test_appium_homework2.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self):

        return MainPage(self.driver)
