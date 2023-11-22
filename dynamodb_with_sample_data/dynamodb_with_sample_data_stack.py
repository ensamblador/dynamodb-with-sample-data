from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    CustomResource,
    CfnOutput
)
from constructs import Construct
from databases import Tables
from lambdas import Lambdas


class DynamodbWithSampleDataStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        T = Tables(self, "T")
        L = Lambdas(self, "L")

        T.sample_table.grant_full_access(L.loader_cr)
        CfnOutput(self, "table", value=T.sample_table.table_name)
        
        ds = CustomResource(
            self,
            "S3DS",
            resource_type="Custom::S3DataSource",
            service_token=L.loader_cr.function_arn,
            properties=dict(
                table_name=T.sample_table.table_name, sample_data_file="dataset.csv"
            ),
        )
        