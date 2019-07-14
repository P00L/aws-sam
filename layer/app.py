import json


def get_response(status, body):
    return {
        "statusCode": status,
        "body": json.dumps(body),
    }
