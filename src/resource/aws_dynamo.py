import ebbs
import eons

@eons.kind(ebbs.Builder)
def aws_dynamo(
	table,
	backupName = "",

	public = eons.public_methods(
		backup = 'aws_dynamo_backup',
		restore = 'aws_dynamo_restore',
	),

	Rollback = lambda this:
		this.restore(this.backupName, this.table),
):
	backupName = backup(table)