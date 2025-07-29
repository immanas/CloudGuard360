import boto3
import datetime
import os

ce = boto3.client('ce')
sns = boto3.client('sns')

SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
THRESHOLD_PERCENT = float(os.environ.get('THRESHOLD_PERCENT', '20'))

def lambda_handler(event, context):
    end = datetime.date.today()
    start = end - datetime.timedelta(days=1)

    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start.isoformat(), 'End': end.isoformat()},
        Granularity='HOURLY',
        Metrics=['UnblendedCost']
    )

    results = response['ResultsByTime'][0]['Groups']
    cost_values = [float(g['Metrics']['UnblendedCost']['Amount']) for g in results]

    if len(cost_values) < 2:
        return {"status": "Not enough data"}

    prev_cost, curr_cost = cost_values[-2], cost_values[-1]
    increase = ((curr_cost - prev_cost) / prev_cost) * 100 if prev_cost else 0

    if increase >= THRESHOLD_PERCENT:
        message = f"[ALERT] Cost ↑ by {increase:.2f}% | Prev: ${prev_cost}, Curr: ${curr_cost}"
        sns.publish(TopicArn=SNS_TOPIC_ARN, Subject="CloudGuard360 Alert", Message=message)
        return {"alert": True, "message": message}

    return {"alert": False, "increase": increase}
