import json
import boto3
# Set the AWS region
AWS_REGION = 'us-east-1'  # Replace 'your_aws_region' with your actual AWS region

# Set up the default session with the AWS region
boto3.setup_default_session(region_name=AWS_REGION)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume-test')

def lambda_handler(event, context):
    response = table.get_item(Key={
        'id':'1'
    })
    views = response['Item']['views']
    views = views + 1
    print(views)
    response = table.put_item(Item={
        'id':'1',
        'views': views
    })
    
    return views