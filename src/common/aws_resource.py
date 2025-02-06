from ebbs import Builder
import eons

# Resources are some stateful thing in AWS.
# Each Resource coordinates a number of Operations.
# Resources must always return themselves to allow for syntax like:
# 	aws.s3("my-bucket").create()
class aws_resource(Builder):

	primaryFunctionName = "SaveState"

	def __init__(this, name = "UNKNOWN AWS RESOURCE"):
		super().__init__(name)
		
		this.requiredKWArgs.append("aws")
		this.enableAutoReturn = True # return *this
