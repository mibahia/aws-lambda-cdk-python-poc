
# This is a template for a CDK Python project

### Why use CDK

Creating infrastructure by interacting by clicking through the several options on the AWS website is not scalable and error prone. 

CDK draws from the "infrastructure as code" framework, ultimately resolving this problem. CDK allows for infrastructure to be created using code (e.g., Python, Typescript or Go), and all the benefits that come with it: the ability to use controlflow, git and auto-complete.

CDK compiles code into a CloudFormation template, which is then used by AWS to create the required infrastructure.

### About this project

This project is a CDK proof of concept written in Python. It downloads a dataset from url and uploads it to a s3 bucket.

### Getting started

To use this infrastructure you'll need to have:

1. AWS account
2. AWS CLI
3. AWS CDK
4. Python

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

There are a few manual steps. In `app.py` add you AWS account id and region. 

The `cdk.json` file tells the CDK Toolkit how to execute your app. In the `UploadRawData` stack change the name of you s3 bucket. 

The first step is to run `cdk bootstrap` which prepares the aws environment and create resources (CloudFormation stack, s3 buckets, sets up trust relationships)to prior to deployment. Only needed one time, after that we just need cdk deploy.

To deploy this lambda run `cdk deploy`. If the deployment is successful, you can test the lambda on AWS, before invoking it. 

To invoke the lambda locally you can run `bash invoke.sh`. You'll need to change the profile, and you may want to test it on a different url. The payload param is the handler event.

#### What this project doesn't have

No endpoint, invoking only happens locally/manually. API Gateway needs to be added.

#### Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Have fun!