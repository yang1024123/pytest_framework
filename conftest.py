import pytest
import requests
import allure

@pytest.fixture(scope='function',autouse=True)
def get_authorization():
    data = {"userName": "yw", "password": "7c9a8efe507000abacdd433dc95645b9"}
    url = "http://10.10.106.250:19971/login"
    try:
        response = requests.post(url=url, json=data)
        response.raise_for_status()
        json_dict = response.json()
        authorization = json_dict['data']
        return authorization
    except requests.exceptions.RequestException as e:
        allure.attach(f"Request failed: {e}", name="Error Log")
        return None