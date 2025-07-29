import boto3
import datetime
import json

def lambda_handler(event, context):
    # Initialize Cost Explorer client
    client = boto3.client('ce')

    # Time range: last 60 days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=60)

    try:
        # Fetch billing data
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost']
        )

        billing_data = []
        for item in response['ResultsByTime']:
            date = item['TimePeriod']['Start']
            amount = float(item['Total']['UnblendedCost']['Amount'])
            billing_data.append({'date': date, 'cost': amount})

        # Add mock usage data
        usage_data = [
            { "service": "Amazon EC2", "usage": "24 vCPU", "cost": "$120.50" },
            { "service": "Amazon S3", "usage": "150 GB", "cost": "$30.10" },
            { "service": "CloudWatch", "usage": "12 Alarms", "cost": "$12.80" }
        ]

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # For frontend CORS
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'usage': usage_data,
                'billing': billing_data
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
