import os
import boto3
from shared import get_response

# env vars set up
TABLE_NAME = os.environ.get("TABLE_NAME", None)

# AWS client set up
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    # retrieve data id
    path_parameters = event["pathParameters"]

    response = table.get_item(Key={"id": path_parameters.get("id")})
    return get_response(200, response["Item"])
