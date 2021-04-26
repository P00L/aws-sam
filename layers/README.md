# A practical guide surviving to AWS SAM part 3 - Lambda Layers

[Medium article]()

This folder contains resources about Lambda Layers.

## Deployment

```shell
sam build
sam deploy --guided
```

From local environment you can test code execution with `tests/tests.py`. Before running test mark directories `layers` 
and `my_layer/python` as source root otherwise python interpreter will not know where to find your code.     

You can also use sam local invoke capabilities

```shell
sam local invoke
```

since in the template there is only on Lambda Function you can avoid to specify the function name