import json
import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')
ce = boto3.client('ce')

def lambda_handler(event, context):
    BUCKET_NAME = 'cloudguard360-ai-data'
    FILE_KEY = 'predicted_cost.json'

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

    threshold = predicted_cost * 1.3
    if actual_cost > threshold:
        message = f"🚨 Anomaly Detected! Actual cost ${actual_cost:.4f} > predicted ${predicted_cost:.4f} (+30%)"
    else:
        message = f"Cost is normal. Actual: ${actual_cost:.4f}, Predicted: ${predicted_cost:.4f}"

    print(message)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "predicted_cost": predicted_cost,
            "actual_cost": actual_cost,
            "status": message
        })
    }
