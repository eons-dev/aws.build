import logging
import json
import eons
from aws_resource import aws_resource

@eons.kind(aws_resource)
def aws_iam_role(
	role_name,
	effect = "Allow",
	principals = ["ec2.amazonaws.com"],
	action = "sts:AssumeRole",
	policy_document = None
):
	client = this.aws.GetClient("iam")

	if (policy_document is None):
		policy_document = {
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": effect,
					"Principal": {"Service": principal for principal in principals},
					"Action": action
				}
			]
		}

	return client.create_role(RoleName = role_name, AssumeRolePolicyDocument = json.dumps(policy_document))
	