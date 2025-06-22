import json
import boto3
import os

stepfunctions = boto3.client('stepfunctions')

# Replace this with your actual Step Function ARN
STEP_FUNCTION_ARN = os.environ.get("STEP_FUNCTION_ARN")

def lambda_handler(event, context):
    """
    Lambda function to trigger the Customer360 Step Function for ETL orchestration.
    """

    # Optional: pass dynamic input to the Step Function
    input_payload = {
        "triggered_by": "lambda",
        "execution_time": context.aws_request_id
    }

    try:
        response = stepfunctions.start_execution(
            stateMachineArn=STEP_FUNCTION_ARN,
            input=json.dumps(input_payload)
        )

        return {
            "statusCode": 200,
            "message": "Step Function execution started",
            "executionArn": response['executionArn']
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }
