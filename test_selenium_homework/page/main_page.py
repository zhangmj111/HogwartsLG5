from selenium.webdriver.common.by import By

from test_selenium_homework.page.basepage import BasePage
from test_selenium_homework.page.contact_list_page import ContactListPage


class MainPage(BasePage):
    def goto_contact_list(self):
        self.find_and_click((By.ID, "menu_contacts"))
        return ContactListPage(self.driver)
