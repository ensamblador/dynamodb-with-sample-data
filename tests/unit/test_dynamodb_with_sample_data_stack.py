import aws_cdk as core
import aws_cdk.assertions as assertions

from dynamodb_with_sample_data.dynamodb_with_sample_data_stack import DynamodbWithSampleDataStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dynamodb_with_sample_data/dynamodb_with_sample_data_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DynamodbWithSampleDataStack(app, "dynamodb-with-sample-data")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
