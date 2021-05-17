# A practical guide surviving to AWS SAM part 3 - Lambda Layers

[Medium article](https://aws.plainenglish.io/a-practical-guide-surviving-aws-sam-part-3-lambda-layers-8a55eb5d2cbe?source=friends_link&sk=26197a231ee55de2f4ee63ea7f1032f0)

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