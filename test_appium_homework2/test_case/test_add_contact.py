import pytest
import yaml

from test_appium_homework2.page.app import App


def get_data():
    with open("../data/data.yml",encoding='utf-8') as f:
        data = yaml.safe_load(f)
        add_data = data["add"]
        return add_data


class TestAddContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name, gender, phone, address", get_data())
    def test_add_contact(self, name, gender, phone, address):
        res = self.main.goto_main().goto_list_contact().goto_add_contact_address().goto_add_contact()\
            .edit_name(name).edit_gender(gender).edit_phone(phone).edit_address(address).save_contact()
        assert "添加成功" == res
