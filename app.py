#!/usr/bin/env python3

import aws_cdk as cdk

from py_cdk_poc.py_cdk_poc_stack import UploadRawData

app = cdk.App()
UploadRawData(
    app,
    "UploadRawData",
    env=cdk.Environment(account="", region="eu-west-2"),
)

app.synth()
