import eons
from aws_operation import aws_operation

@eons.kind(aws_operation)
def aws_dynamo_table_item_put(
	values = {}
):
	client = this.aws.GetClient("dynamodb")

	# Assume aws.dynamo.table.item.put
	tableResource = caller.caller

	primaryKeyName = tableResource.get_keys().result.data.hashKey
	itemData = values.update({primaryKeyName: caller.key})
	
	response = client.put_item(
		TableName = caller.table,
		Item = itemData,
	)
	this.result.data = eons.util.DotDict(response)