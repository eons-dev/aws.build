import logging
import eons
from aws_resource import aws_resource

@eons.kind(aws_resource)
def aws_iam_bucket_policy(
	group,
	bucket_name,
	bucket,
	policy_document_name,
	policy_document = None
):
	client = this.aws.GetClient("iam")
		
	if (policy_document is None):
		policy_document = f'''\
{{
	"Version": "2012-10-17",
	"Statement": [
		{{
			"Effect": "Allow",
			"Action": "s3:*",
			"Resource": [
				"arn:aws:s3:::{bucket}/*"
			]
		}}
	]
}}
'''
	logging.debug(f"Bucket Policy: {policy_document}")

	policy_document_arn = f"arn:aws:iam::{this.aws.GetAccountId()}:policy/{policy_document_name}"

	policyExists = False
	try:
		response = client.get_policy(PolicyArn=policy_document_arn)
		logging.debug(f"Bucket Policy ARN: {response['Policy']['Arn']}")
		policyExists = True
	except:
		pass
	
	if (policyExists):
		response = client.create_policy_version(
			PolicyArn = policy_document_arn,
			PolicyDocument = policy_document,
			SetAsDefault= True
		)
		versionId = response["PolicyVersion"]["VersionId"]
		versionToDelete = int(versionId[1:]) - 1
		client.delete_policy_version(PolicyArn = policy_document_arn, VersionId = f"v{versionToDelete}")
	else:
		response = client.create_policy(
			PolicyName=policy_document_name,
			PolicyDocument=policy_document
		)
		logging.debug(f"Bucket Policy ARN: {response['Policy']['Arn']}")

	client.attach_group_policy(GroupName=group, PolicyArn=policy_document_arn)
