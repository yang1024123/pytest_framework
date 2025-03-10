import json

import requests
import pytest
import allure


def get_authorization():
    data = {"userName": "yw", "password": "7c9a8efe507000abacdd433dc95645b9"}
    url = "http://10.10.106.250:19971/login"
    try:
        response = requests.post(url=url, json=data)
        response.raise_for_status()
        json_dict = response.json()
        authorization = json_dict['data']
        print(authorization,type(authorization))
        return authorization
    except requests.exceptions.RequestException as e:
        allure.attach(f"Request failed: {e}", name="Error Log")
        return None


@pytest.mark.parametrize("authorization",[get_authorization()])
def test_fixture(authorization):
    headers = {
        'authorization': authorization,
        'Content-Type': 'application/json;charset=UTF-8',
    }
    data = {"caseType":0,"name":"这是案例333","faultLastTime":41}
    url = "http://10.10.106.250:19971/caseRule/svg-list/by-fault-type"
    try:
        response = requests.post(url=url, json=data,headers=headers)
        response_dict = response.json()
        file_doc_ids = ""
        for item in response_dict['data']:
            print(item["fileDocId"], type(item["fileDocId"]))
            file_doc_ids += "," + item["fileDocId"]
        return file_doc_ids
    except requests.exceptions.RequestException as e:
        allure.attach(f"Request failed: {e}", name="Error Log")
        return None