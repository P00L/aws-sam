import json

import pytest

from part_1.hello_world import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""
    with open("../../event.json") as json_file:
        return json.load(json_file)


def test_lambda_handler(apigw_event, mocker):
    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world!"
    # assert "location" in data.dict_keys()
