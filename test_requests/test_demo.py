import json

import requests


def test_demo():
    #获取token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=jjx12e171a30e32dg2&corpsecret=_4fQ_bIh6Hli7v8R5-MzjtDFrLPcJQ8DDJeFxk5SDad"
    r = requests.get(url)
    token = r.json()["access_token"]
    #读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=LiSi"
    r = requests.get(url)
    result = r.json()["errmsg"]
    assert result == "ok"
    #更新成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "lisi",
        "name": "里斯"
    }
    r = requests.post(url, json=body)
    result = r.json()["errmsg"]
    assert result == "updated"
    # #创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "xiaocilang",
        "name": "小次郎",
        "mobile": "+86 13800000001",
        "department": [1]
    }
    header = {
        "content-type": "application/json"
    }
    r = requests.post(url, data=json.dumps(body), headers=header)
    result = r.json()["errmsg"]
    assert result == "created"
    #删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=xiaocilang"
    r = requests.get(url)
    result = r.json()["errmsg"]
    assert result == "deleted"
