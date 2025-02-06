import eons
import logging
from aws_resource import aws_resource

@eons.kind(eons.Functor)
def aws_dynamo_table_rollback():
	caller.rollbackSucceeded = True
	if (not hasattr(caller.backup.result.data.BackupArn)):
		caller.rollbackSucceeded = False
		return
	
	response = caller.restore(
		TargetTableName = caller.table,
		BackupArn = caller.backup.result.data.BackupArn
	)

	caller.result.data.rollback = eons.util.DotDict(response)

@eons.kind(aws_resource)
def aws_dynamo_table(
	table,
	require_backup = True, # more work on create but safer overall

	public = eons.public_methods(
		Rollback = 'aws_dynamo_table_rollback',
	),
):
	# Backups are nice, but not always necessary.
	# Maybe the table doesn't exist yet & that's our job.
	try:
		backup(table)
	except Exception as e:
		errorMessage = f"Failed to backup table {table}: {e}"
		if (require_backup):
			logging.error(errorMessage)
			raise e
		else:
			logging.warning(errorMessage)