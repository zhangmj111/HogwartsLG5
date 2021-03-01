import requests


class Base:
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwc12e171a30e22af2&corpsecret=_7lQ_bIh6Hli7v8R5-MzjtDMrLPcJQ8CQJeFxk5SDbw"
        r = requests.request("get", url).json()
        self.token = r["access_token"]
        self.request_session = requests.Session()
        self.request_session.params = {"access_token": self.token}

    def send(self, *args, **kwargs):
        r = self.request_session.request(*args, **kwargs)
        return r.json()

