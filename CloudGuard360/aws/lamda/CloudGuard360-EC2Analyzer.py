import boto3
import datetime
import json

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

S3_BUCKET = 'cloudguard360-usage-logs'  # replace with your bucket name

def lambda_handler(event, context):
    response = ec2.describe_instances()
    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_data = {
                "InstanceId": instance['InstanceId'],
                "InstanceType": instance['InstanceType'],
                "State": instance['State']['Name'],
                "LaunchTime": instance['LaunchTime'].isoformat()
            }
            instances.append(instance_data)

    # Prepare file content and filename
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    filename = f'ec2-usage-{timestamp}.json'
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=filename,
        Body=json.dumps(instances),
        ContentType='application/json'
    )

    return {"saved_to_s3": filename, "count": len(instances)}
