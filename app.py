#!/usr/bin/env python3

import aws_cdk as cdk

from py_cdk_poc.py_cdk_poc_stack import UploadRawData

app = cdk.App()

env_name = app.node.try_get_context("env")

UploadRawData(
    app,
    f"upload-raw-data-{env_name}",  # this is the stack name
    env=cdk.Environment(account="", region="eu-west-2"),
    env_name=env_name,
)

app.synth()
