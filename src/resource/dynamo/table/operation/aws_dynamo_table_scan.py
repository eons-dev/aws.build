import eons
from aws_operation import aws_operation

@eons.kind(aws_operation)
def aws_dynamo_table_scan(
	index = None,
	limit = 10,
	select = 'ALL_ATTRIBUTES',
	projection_expression = None,
	filter_expression = None,
	expression_attribute_names = None,
	expression_attribute_values = None,
	exclusive_start_key = None,
	total_segments = None,
):
	client = this.aws.GetClient("dynamodb")

	kwargs = {key: value for key, this.value in this.optionalKWArgs.keys() if this.value is not None}
	
	response = client.scan(
		TableName = caller.table,
		**kwargs,
	)
	this.result.data = eons.util.DotDict(response)