import eons
import logging
from aws_resource import aws_resource

@eons.kind(eons.Functor)
def aws_dynamo_rollback():
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
def aws_dynamo(
	table,

	public = eons.public_methods(
		Rollback = 'aws_dynamo_rollback',
		backup = 'aws_dynamo_backup',
		restore = 'aws_dynamo_restore',
	),
):
	# Backups are nice, but not always necessary.
	# Maybe the table doesn't exist yet & that's our job.
	try:
		backup(table)
	except Exception as e:
		logging.warning(f"Failed to backup table {table}: {e}")