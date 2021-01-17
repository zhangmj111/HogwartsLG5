from selenium.webdriver.common.by import By

from test_selenium_homework.page.basepage import BasePage


class AddDepartmentPage(BasePage):
    def edit_department(self):
        self.find_and_sendkeys((By.XPATH, "//*[@class='inputDlg_item'][1]//input"), "第四部门")
        self.find_and_click((By.LINK_TEXT, "选择所属部门"))
        self.find_and_click((By.XPATH,
                            "//*[@class='qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container']//*[@id='1688853095533257_anchor']"))
        return self

    def save_department(self):
        from test_selenium_homework.page.contact_list_page import ContactListPage
        self.find_and_click((By.LINK_TEXT, "确定"))
        return ContactListPage(self.driver)
