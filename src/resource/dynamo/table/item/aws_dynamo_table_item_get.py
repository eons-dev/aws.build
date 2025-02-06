import eons
from aws_operation import aws_operation

@eons.kind(aws_operation)
def aws_dynamo_table_item_get():
	client = this.aws.GetClient("dynamodb")
	
	response = client.get_item(
		TableName = caller.table,
		Key = caller.key,
	)
	this.result.data = eons.util.DotDict(response)