import json

HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
}


def get_response(code, body):
    return {
        "statusCode": code,
        "headers": HEADERS,
        "body": json.dumps(body)
    }
