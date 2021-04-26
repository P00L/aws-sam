import json
# import say_hello from my_common_function layer (my_layer)
# remember to mark my_layer/python folder as source directory to get rid of import error
from my_common_function import say_hello


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": say_hello() # invoke layer function
        }),
    }
