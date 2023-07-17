import eons

@eons.kind(eons.Functor)
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