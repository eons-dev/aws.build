import eons

@eons.kind(eons.Functor)
def aws_dynamo_table_get_keys():
	client = this.aws.GetClient("dynamodb")
	tableDescription = client.describe_table(TableName = caller.table)
	keySchema = tableDescription['Table']['KeySchema']
	hashKey = None
	rangeKey = None
	for key in keySchema:
		if key['KeyType'] == 'HASH':
			hashKey = key['AttributeName']
		elif key['KeyType'] == 'RANGE':
			rangeKey = key['AttributeName']
	
	this.result.data.hashKey = hashKey
	this.result.data.rangeKey = rangeKey