from aws_resource import aws_resource
import eons

@eons.kind(aws_resource)
def aws_dynamo_restore(
	backup,
	table,
):
	client = this.aws.GetClient("dynamodb")

	client.restore_table_from_backup(
		BackupArn = backup,
		TargetTableName = table
	)