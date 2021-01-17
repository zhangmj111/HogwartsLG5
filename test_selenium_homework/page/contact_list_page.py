from selenium.webdriver.common.by import By

from test_selenium_homework.page.add_department_page import AddDepartmentPage
from test_selenium_homework.page.basepage import BasePage


class ContactListPage(BasePage):
    def goto_add_department(self):
        self.find_and_click((By.CSS_SELECTOR, ".member_colLeft_top_addBtn"))
        self.find_and_click((By.LINK_TEXT, "添加部门"))
        return AddDepartmentPage(self.driver)

    def get_department(self):
        result = self.find((By.ID, "js_tips")).text
        return result
