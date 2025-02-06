import eons
from aws_operation import aws_operation

@eons.kind(aws_operation)
def aws_dynamo_backup(
	table,
	backup_name,
):
	client = this.aws.GetClient("dynamodb")
	
	response = client.create_backup(
		TableName = table,
		BackupName = backup_name
	)
	this.result.data = eons.util.DotDict(response["BackupDetails"])