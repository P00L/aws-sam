import sys
import os

# adding PYTHONPATH for absolute import running test from CLI
base_path = f"/{os.path.join(*os.path.realpath(__file__).split('/')[:-2])}"
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, 'layer'))

import os
import json
import pytest
import boto3
import insert_data.app as lambda_module
from dataclasses import dataclass

TABLE_NAME = os.environ.get("TABLE_NAME", None)

# simulate Lambda context
@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:test"
        aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

    return LambdaContext()


def test_insert_data(lambda_context):
    f = open("events/InsertData.json", "r")
    event = json.loads(f.read())

    response_lambda = lambda_module.lambda_handler(event, lambda_context)
    assert response_lambda["statusCode"] == 200

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)
    response_secret = table.get_item(Key={"id": json.loads(response_lambda["body"])["data_id"]})

    assert response_secret["Item"]["my_data"] == "this is a sample data"
