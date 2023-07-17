import eons
from aws_resource import aws_resource

@eons.kind(aws_resource)
def aws_s3(
	bucket_name,

	public = eons.public_methods(
		create = "aws_s3_create",
	)
):
	pass