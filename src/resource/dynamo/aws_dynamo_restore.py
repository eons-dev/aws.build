from aws_operation import aws_operation
import eons

@eons.kind(aws_operation)
def aws_dynamo_restore(
	backup,
	table,
):
	client = this.aws.GetClient("dynamodb")

	client.restore_table_from_backup(
		BackupArn = backup,
		TargetTableName = table
	)