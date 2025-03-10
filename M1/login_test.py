import requests
import json
import allure

@allure.feature("登录")
def test_login_success():
    raw_data = '{"userName":"yw","password":"7c9a8efe507000abacdd433dc95645b9"}'
    data = json.loads(raw_data)

    url = "http://10.10.106.250:19971/login"
    response = requests.post(url=url, json=data)
    assert response.status_code == 200
@allure.feature("不存在用户登录")
def test_login_inexistentUser():
    raw_data = '{"userName":"YW123","password":"7c9a8efe507000abacdd433dc95645b9"}'
    data = json.loads(raw_data)

    url = "http://10.10.106.250:19971/login"
    response = requests.post(url=url, json=data)
    assert "用户名不存在" in response.text
@allure.feature("错误密码登录")
def test_login_errorPwd():
    raw_data = '{"userName":"yw","password":"1234"}'
    data = json.loads(raw_data)

    url = "http://10.10.106.250:19971/login"
    response = requests.post(url=url, json=data)
    assert "密码错误" in response.text


@allure.feature("退出登录")
def test_loginout(get_authorization):
    url = "http://10.10.106.250:19971/logout"
    headers = {
        'authorization': get_authorization
    }

    url = "http://10.10.106.250:19971/logout"
    response = requests.post(url=url, headers=headers)
    assert "用户已注销" in response.text