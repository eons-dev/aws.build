import eons
from aws_resource import aws_resource

@eons.kind(aws_resource)
def aws_dynamo_table_item(
	key,
	table,
):
	pass