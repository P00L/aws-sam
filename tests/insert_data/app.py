import os
import json
import boto3
import uuid
from shared import get_response

# env vars set up
TABLE_NAME = os.environ.get("TABLE_NAME", None)

# AWS client set up
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event: dict, context: object):
    body = json.loads(event["body"])
    data_id = str(uuid.uuid4())
    body['id'] = data_id

    table.put_item(
        Item=body
    )

    return get_response(200, {"data_id": data_id})
