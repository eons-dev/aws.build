import eons

@eons.kind(eons.Functor)
def aws_ec2(
	public = eons.public_methods(
		security_group = "aws_ec2_security_group"
	)
):
	pass