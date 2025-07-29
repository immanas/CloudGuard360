import json
import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')
ce = boto3.client('ce')
sns = boto3.client('sns')

# Use your existing SNS topic
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:713881803439:CloudGuard360CostAlerts'

def lambda_handler(event, context):
    BUCKET_NAME = 'cloudguard360-ai-data'
    FILE_KEY = 'predicted_cost.json'

    # Step 1: Load predicted cost from S3
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
        content = response['Body'].read().decode('utf-8')
        predicted_data = json.loads(content)
        predicted_cost = predicted_data['predicted_cost']
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error loading predicted cost: {str(e)}"
        }

    # Step 2: Get yesterday's actual cost from AWS Cost Explorer
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)

    try:
        cost_response = ce.get_cost_and_usage(
            TimePeriod={
                'Start': str(yesterday),
                'End': str(today)
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost']
        )
        actual_cost = float(cost_response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error fetching actual cost: {str(e)}"
        }

    # Step 3: Compare costs
    threshold = predicted_cost * 1.3  # 30% higher than predicted
    if actual_cost > threshold:
        message = (
            f"🚨 Anomaly Detected by AI!\n"
            f"Date: {yesterday}\n"
            f"Predicted Cost: ${predicted_cost:.4f}\n"
            f"Actual Cost: ${actual_cost:.4f}\n"
            f"Exceeded threshold by more than 30%!"
        )
        # 🚨 Trigger SNS alert
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="[CloudGuard360] Billing Anomaly Alert",
            Message=message
        )
    else:
        message = (
            f"✅ Cost is normal.\n"
            f"Date: {yesterday}\n"
            f"Predicted: ${predicted_cost:.4f}\n"
            f"Actual: ${actual_cost:.4f}"
        )

    print(message)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "predicted_cost": predicted_cost,
            "actual_cost": actual_cost,
            "status": message
        })
    }
