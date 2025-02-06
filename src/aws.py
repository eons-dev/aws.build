from ebbs import Builder
import eons
import boto3
import logging

@eons.kind(eons.Functor)
def aws_GetAccount():
	#FIXME: @Amazon, WTF? Why is this so hard???

	this.result.data.id = None
	this.result.data.alias = None
	this.result.data.orgName = None
	
	this.result.data.best = eons.util.DotDict()
	this.result.data.best.id = None
	this.result.data.best.source = None

	try:
		this.result.data.id = caller.GetClient("sts").get_caller_identity().get("Account")
		this.result.data.best.source = "sts"
		this.result.data.best.id = this.data.result.id
	except:
		pass

	try:
		this.result.data.best.orgName = this.aws.GetClient("organizations").describe_account(AccountId='<account-id>').get('Account').get('Name')
		this.result.data.best.source = "org"
		this.result.data.best.id = this.result.data.orgName
	except:
		pass

	try:
		this.result.data.alias = caller.GetClient("iam").list_account_aliases().get("AccountAliases")[0]
		this.result.data.best.source = "iam"
		this.result.data.best.id = this.result.data.alias
	except:
		pass

@eons.kind(eons.Functor)
def aws_CreateSession():
	caller.session = boto3.session.Session(
		aws_access_key_id=caller.aws_access_key_id,
		aws_secret_access_key=caller.aws_access_key_secret,
		region_name=caller.aws_region
	)
	logging.info(f"Logged into AWS as account {caller.GetAccount().result.data.best.id} ({caller.GetAccount.result.data.best.source})")

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

	session = None,

	public = eons.public_methods(
		GetAccount = "aws_GetAccount",
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
	CreateSession()

