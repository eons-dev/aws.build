import eons

@eons.kind(eons.Functor)
def aws_s3(
	public = eons.public_methods(
		bucket = "aws_s3_bucket"
	)
):
	pass