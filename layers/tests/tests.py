# remember to set root folder [layers] as source root folder
from hello_world.app import lambda_handler

# we don't need event nor context we can pass None as parameters
response = lambda_handler(None, None)
print(response)
