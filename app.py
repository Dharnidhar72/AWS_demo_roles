#!/usr/bin/env python3
import os
from aws_cdk import App, Environment
from aws_role_stack import MskAdminRoleStack

# Define environment variables if needed
env = Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"])
)

app = App()

# Create an instance of the MSK Admin role stack
MskAdminRoleStack(
    app, 
    "MskAdminRoleStack",
    env=env,
    description="Stack that creates an MSK Admin role with AmazonMSKFullAccess permissions"
)

app.synth()