from test_selenium_homework.page.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()
    def test_add_department(self):
        result = self.main.goto_contact_list().goto_add_department().edit_department().save_department().get_department()
        assert "新建部门成功" == result
