import requests

from test_requests2.api.base import Base


class Address(Base):
    # 创建成员
    def add_member(self, userid, name, mobile, department, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        body.update(kwargs)
        r = self.send("post", url, json=body)
        return r["errcode"]

    # 读取成员
    def detect_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        r = self.send("get", url)
        return r["errcode"]

    # 更新成员
    def update_member(self, userid, name, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name,
        }
        body.update(kwargs)
        r = self.send("post", url, json=body)
        return r["errcode"]

    # 删除成员
    def delete_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        r = self.send("get", url)
        return r["errcode"]
