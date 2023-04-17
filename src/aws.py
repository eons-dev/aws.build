from ebbs import Builder
import boto3
import logging

class aws(Builder):
	def __init__(this, name="AWS"):
		super().__init__(name)
		
		this.requiredKWArgs.append("aws_access_key_id")
		this.requiredKWArgs.append("aws_access_key_secret")
		
		this.optionalKWArgs["aws_region"] = "us-east-1"

	def CreateSession(this):
		this.session = boto3.session.Session(
			aws_access_key_id_id=this.aws_access_key_id,
			aws_secret_access_key=this.aws_access_key_secret,
			region_name=this.aws_region
		)
		logging.info(f"Logged into AWS as account {this.GetClient('sts').get_caller_identity().get('Account')}")

	def GetClient(this, service):
		if (this.session is None):	
			return boto3.client(
				service,
				aws_access_key_id_id=this.aws_access_key_id,
				aws_secret_access_key=this.aws_access_key_secret,
				region_name=this.aws_region
			)
		return this.session.client(service)

	def Build(this):
		this.CreateSession()