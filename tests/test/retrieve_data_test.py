import sys
import os

# adding PYTHONPATH for absolute import running test from CLI
base_path = f"/{os.path.join(*os.path.realpath(__file__).split('/')[:-2])}"
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, 'layer'))

import json
import pytest
import os
import boto3
from dataclasses import dataclass
import retrieve_data.app as lambda_module
from botocore import stub

TABLE_NAME = os.environ.get('TABLE_NAME', None)


# simulate Lambda context for Lambda
@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:test"
        aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

    return LambdaContext()


# fixture executed once on module startup for DynamoDB table initialization
@pytest.fixture(scope='module', autouse=True)
def setup():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)

    response_data = table.get_item(Key={"id": "test"})

    if "Item" in response_data:
        table.delete_item(Key={"id": "test"})

    table.put_item(
        Item={
            "id": "test",
            "my_data": "this is a sample data",
        }
    )

    yield

    table.delete_item(Key={"id": "test"})


def test_retrieve_lambda(lambda_context):
    f = open("events/RetrieveData.json", "r")
    event = json.loads(f.read())

    response_lambda = lambda_module.lambda_handler(event, lambda_context)
    assert response_lambda["statusCode"] == 200


def test_retrieve_lambda_stub(lambda_context):
    f = open("events/RetrieveData.json", "r")
    event = json.loads(f.read())

    stubber = stub.Stubber(lambda_module.table.meta.client)

    # mocking dynamodb call to get_item
    stubber.add_response(
        'get_item', {
            'Item':
                {'id':
                     {'S': 'test'},
                 'my_data':
                     {'S': 'this is a sample data'}
                 }}
    )

    stubber.activate()

    response_lambda = lambda_module.lambda_handler(event, lambda_context)
    assert response_lambda["statusCode"] == 200

    stubber.deactivate()
