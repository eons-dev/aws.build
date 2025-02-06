import eons

import ebbs
import eons
import logging

@eons.kind(ebbs.Builder)
def aws_test_login():
	this.aws = this.executor.Execute("aws")
	assert(this.aws.GetAccount.result.data.best.id != None)
