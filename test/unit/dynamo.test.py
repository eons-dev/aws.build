import ebbs
import eons
import logging
from aws import aws

@eons.kind(ebbs.Builder)
def aws_test_dynamo():
	this.aws = aws()

	this.aws.dynamo.table("TEST_TABLE_DELETEME", require_backup = False).create(
		attribute_definitions = [
			{
				"AttributeName": "id",
				"AttributeType": "S"
			},
		],
		key_schema = [
			{
				"AttributeName": "id",
				"KeyType": "HASH"
			},
		],
		provisioned_throughput = {
			"ReadCapacityUnits": 1,
			"WriteCapacityUnits": 1
		}
	)
	logging.debug(this.aws.dynamo.create.result.data)

	primaryKey = this.aws.dynamo.table("TEST_TABLE_DELETEME").get_keys().result.data.hashKey

	this.aws.dynamo.table("TEST_TABLE_DELETEME").item("DELETEME_TOO").put({
		'value': {
			'S': 'test'
		}
	})

	tableItems = this.aws.dynamo.table("TEST_TABLE_DELETEME").scan().result.data
	assert(tableItems.Count == 1)

	itemData = this.aws.dynamo.table("TEST_TABLE_DELETEME").item(tableItems[0][primaryKey]['S']).get().result.data
	assert(itemData.Item['value']['S'] == 'test')

	# Attempt to force a failure & make sure rolling back works
	this.aws.dynamo.table.raiseExceptions = False
	this.aws.dynamo.table("TEST_TABLE_DELETEME").item("DELETEME_TOO").put("bad data")

	# Make sure the rollback worked
	tableItems = this.aws.dynamo.table("TEST_TABLE_DELETEME").scan().result.data
	assert(tableItems.Count == 1)

	itemData = this.aws.dynamo.table("TEST_TABLE_DELETEME").item(tableItems[0][primaryKey]['S']).get().result.data
	assert(itemData.Item['value']['S'] == 'test')

	# Now delete the table
	this.aws.dynamo.table("TEST_TABLE_DELETEME").delete()
