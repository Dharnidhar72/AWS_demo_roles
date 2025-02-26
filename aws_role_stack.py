from aws_cdk import (
    Stack,
    aws_iam as iam,
    CfnOutput
)
from constructs import Construct
from constants import IAM_USER_ARN

class MskAdminRoleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the MSK Admin role for a single IAM user
        msk_admin_role = iam.Role(
            self, 
            "MskAdminRole",
            assumed_by=iam.ArnPrincipal(IAM_USER_ARN),
            description="Role for MSK Admin with limited permissions",
            role_name="MskAdminRole"
        )
        
        # Attach the AWS managed AmazonMSKFullAccess policy
        msk_admin_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonMSKFullAccess")
        )
        
        # Export the role ARN as an output
        CfnOutput(
            self,
            "MskAdminRoleArn",
            description="The ARN of the MSK Admin role",
            value=msk_admin_role.role_arn
        )