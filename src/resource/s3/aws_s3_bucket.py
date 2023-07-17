from aws_resource import aws_resource
import eons

@eons.kind(aws_resource)
def aws_s3_bucket(
	bucket_name,
	bucket_acl = "private",
	bucket_versioning = "Enabled", # or "Suspended"
	bucket_encryption = "AES256"
):
	client = tf.aws.GetClient("s3")

	try:
		client.head_bucket(Bucket=bucket_name)
	except:
		kwargs = {"Bucket": bucket_name}
		if (this.aws.aws_region not in ["us-east-1"]):
			kwargs["CreateBucketConfiguration"] = {"LocationConstraint": this.aws.aws_region}
		client.create_bucket(**kwargs)

	client.put_bucket_acl(Bucket=bucket_name, ACL=bucket_acl)
	client.put_bucket_versioning(
		Bucket=bucket_name, 
		VersioningConfiguration={"Status": bucket_versioning}
	)
	client.put_bucket_encryption(
		Bucket=bucket_name,
		ServerSideEncryptionConfiguration={
			"Rules": [{
				"ApplyServerSideEncryptionByDefault": {
					"SSEAlgorithm": bucket_encryption
				}
			}]
		}
	)