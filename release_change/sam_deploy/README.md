# SAM deploy pipeline

## Pipeline creation

```shell
aws cloudformation create-stack \
    --stack-name sam-deploy-pipeline \
    --template-body file://pipeline_template.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```

## Application deployment

Deployment will be managed by the pipeline at each push