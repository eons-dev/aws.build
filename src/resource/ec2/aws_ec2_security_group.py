import logging
import json
import eons
from aws_resource import aws_resource

@eons.kind(aws_resource)
def aws_ec2_security_group():
	pass