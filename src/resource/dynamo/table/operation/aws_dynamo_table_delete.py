import eons
from aws_operation import aws_operation

@eons.kind(aws_operation)
def aws_dynamo_delete():
	client = this.aws.GetClient("dynamodb")
	
	response = client.delete_table(
		TableName = caller.table,
	)
	this.result.data = eons.util.DotDict(response)