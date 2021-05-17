# A practical guide surviving to AWS SAM part 4 - Release Change

[Medium article]()

This folder contains resources about CodePipeline Release Change for AWS SAM. 

## [SAM deploy pipeline](sam_deploy)

Pipeline with build package and deploy performed by CodeBuild

![sam deploy](images/sam-deploy.png)


## [CloudFormation deploy](cf_deploy)

Pipeline with build and package performed by CodeBuild while deployment managed by CloudFormation action embedded in
CodePipeline

![Cloudformation deploy](images/cf-deploy.png)

