import json
from ssm_cache import SSMParameter
from aws_lambda_powertools.utilities import parameters
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get("LOG_LEVEL"))

my_ssm_parameter_ssm_cache = SSMParameter("MyParameter").value
my_ssm_parameter_powertools = parameters.get_parameter("/MyParameter")


def lambda_handler(event, context):
    # Environment section of SAM template
    logger.info(f"ENV = {os.environ.get('ENV')}")
    logger.info(f"MY_SSM_PARAMETER_RESOLVE = {os.environ.get('MY_SSM_PARAMETER_RESOLVE')}")
    logger.info(f"MY_SSM_PARAMETER = {os.environ.get('MY_SSM_PARAMETER')}")
    logger.info(f"my_ssm_parameter_ssm_cache = {my_ssm_parameter_ssm_cache}")
    logger.info(f"my_ssm_parameter_powertools = {my_ssm_parameter_powertools}")
    logger.info(f"MY_SECRET = {os.environ.get('MY_SECRET')}")
    logger.info(f"LOG_LEVEL = {os.environ.get('LOG_LEVEL')}")
    logger.info(f"LOG_LEVEL_MAPPING = {os.environ.get('LOG_LEVEL_MAPPING')}")
    logger.info(f"LOG_LEVEL_CONDITION = {os.environ.get('LOG_LEVEL_CONDITION')}")

    # Change LOG_LEVEL environment variable to test log level behaviour
    logger.info("this is an INFO message")
    logger.debug("this is a DEBUG message")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world!"
        }),
    }
