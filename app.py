#!/usr/bin/env python3

from aws_cdk import core

from qpythonlambdaStack import qpythonlambdaStack

app = core.App()
qpythonlambdaStack(app, "qpython-lambda-cdk", env={'region': 'us-east-1'})

app.synth()
