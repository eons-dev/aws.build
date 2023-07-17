from aws_operation import aws_operation
import eons

@eons.kind(aws_operation)
def aws_s3_bucket(
	bucket_acl = "private",
	bucket_versioning = "Enabled", # or "Suspended"
	bucket_encryption = "AES256"
):
	client = this.aws.GetClient("s3")

	try:
		client.head_bucket(Bucket=caller.bucket_name)
	except:
		kwargs = {"Bucket": caller.bucket_name}
		if (this.aws.aws_region not in ["us-east-1"]):
			kwargs["CreateBucketConfiguration"] = {"LocationConstraint": this.aws.aws_region}
		client.create_bucket(**kwargs)

	client.put_bucket_acl(Bucket=caller.bucket_name, ACL=bucket_acl)
	client.put_bucket_versioning(
		Bucket=caller.bucket_name, 
		VersioningConfiguration={"Status": bucket_versioning}
	)
	client.put_bucket_encryption(
		Bucket=caller.bucket_name,
		ServerSideEncryptionConfiguration={
			"Rules": [{
				"ApplyServerSideEncryptionByDefault": {
					"SSEAlgorithm": bucket_encryption
				}
			}]
		}
	)