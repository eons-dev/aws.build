import eons
from aws_resource import aws_resource

# TODO:IAM Likely needs another resource level, like iam.role("my-role").create()

@eons.kind(aws_resource)
def aws_iam(
	public = eons.public_methods(
		role = "aws_iam_role",
		bucket_policy = "aws_iam_bucket_policy",
		# user = "aws_iam_user",
		# group = "aws_iam_group",
		# policy = "aws_iam_policy",
	)
):
	pass