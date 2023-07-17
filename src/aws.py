from ebbs import Builder
import eons
import boto3
import logging

@eons.kind(eons.Functor)
def aws_GetAccountId():
	return caller.GetClient("sts").get_this_identity().get("Account")

@eons.kind(eons.Functor)
def aws_CreateSession():
	caller.session = boto3.session.Session(
		aws_access_key_id=caller.aws_access_key_id,
		aws_secret_access_key=caller.aws_access_key_secret,
		region_name=caller.aws_region
	)
	logging.info(f"Logged into AWS as account {caller.GetAccountId()}")

@eons.kind(eons.Functor)
def aws_GetClient(service):
	if (caller.session is None):
		return boto3.client(
			service,
			aws_access_key_id=caller.aws_access_key_id,
			aws_secret_access_key=caller.aws_access_key_secret,
			region_name=caller.aws_region
		)
	return caller.session.client(service)

@eons.kind(Builder)
def aws(
	aws_access_key_id,
	aws_access_key_secret,
	aws_region = "us-east-1",	

	public = eons.public_methods(
		GetAccountId = "aws_GetAccountId",
		CreateSession = "aws_CreateSession",
		GetClient = "aws_GetClient",
		s3 = "aws_s3",
		iam = "aws_iam",
		dynamo = "aws_dynamo"
	),

	constructor = f"""\
this.aws = this
"""
):
	return CreateSession()

