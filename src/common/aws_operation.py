from ebbs import Builder
import eons

# Operations are sub-categories of resources.
# They represent actions a user may take & are coordinated by the resource.
@eons.kind(Builder)
def aws_operation(aws):
	pass