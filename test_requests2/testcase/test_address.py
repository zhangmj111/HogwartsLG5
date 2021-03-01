import pytest

from test_requests2.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    # 创建成员
    @pytest.mark.parametrize("userid,name,mobile,department", [["xiaose", "小色", "+86 13800000002", [1]]])
    def test_add_member(self, userid, name, mobile, department):
        self.address.delete_member(userid)
        result = self.address.add_member(userid, name, mobile, department)
        assert result == 0

    # 读取成员
    @pytest.mark.parametrize("userid", ["lisi"])
    def test_detect_member(self, userid):
        result = self.address.detect_member(userid)
        assert result == 0

    # 更新成员
    @pytest.mark.parametrize("userid,name,position", [["LiSi", "李四", "打杂的"]])
    def test_update_member(self, userid, name, position):
        result = self.address.update_member(userid, name, position=position)
        assert result == 0

    # 删除成员
    @pytest.mark.parametrize("userid", ["xiaose"])
    def test_delete_member(self, userid):
        result = self.address.delete_member(userid)
        assert result == 0