#!/usr/bin/env python3

import aws_cdk as cdk

from py_cdk_poc.py_cdk_poc_stack import UploadRawData

app = cdk.App()

UploadRawData(
    app,
    "upload-raw-data",  # this is the stack name
    env=cdk.Environment(account="", region="eu-west-2"),
)

app.synth()
