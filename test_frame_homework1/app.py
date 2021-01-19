from appium import webdriver

from test_frame_homework1.basepage import BasePage
from test_frame_homework1.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
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
