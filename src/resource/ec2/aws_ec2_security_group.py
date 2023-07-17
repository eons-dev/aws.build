import logging
import json
import eons
from aws_operation import aws_operation

@eons.kind(aws_operation)
def aws_ec2_security_group():
	pass