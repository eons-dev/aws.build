import eons
from aws_operation import aws_operation

@eons.kind(aws_operation)
def aws_dynamo_create(
	attribute_definitions,
	key_schema,
	provisioned_throughput,
	global_secondary_indexes = None,
	local_secondary_indexes = None,
	stream_specification = None,
	sse_specification = None,
	tags = None,
):
	client = this.aws.GetClient("dynamodb")

	response = client.create_table(
		TableName = caller.table,
		AttributeDefinitions = attribute_definitions,
		KeySchema = key_schema,
		ProvisionedThroughput = provisioned_throughput,
		GlobalSecondaryIndexes = global_secondary_indexes,
		LocalSecondaryIndexes = local_secondary_indexes,
		StreamSpecification = stream_specification,
		SSESpecification = sse_specification,
		Tags = tags,
	)

	this.result.data = eons.util.DotDict(response["TableDescription"])