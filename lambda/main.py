import json
from botocore.exceptions import ClientError 
import math
import boto3
import time
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    
    AWS_ACCESS_KEY="Enter Access Key Here"
    AWS_SECRET_ACCESS_KEY="Enter Secret Access Key Here"
    AWS_REGION="Enter region here"
    DYNAMODB_TABLE='Enter Dynamodb table here'
    
    ses = boto3.client('ses',
                           region_name=AWS_REGION,
                           aws_access_key_id= AWS_ACCESS_KEY,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
                           
    dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
                            
    table = dynamodb.Table(DYNAMODB_TABLE)

    now = int(time.time())
    timestampold = now - 60 #only checks values from the last minute

    response = table.scan(
        FilterExpression=Key('stationID').eq('mbed1') & Attr('timestamp').gt(timestampold) #will only extract data from mbed1 device from the past 60 seconds
    )

    items = response['Items']
    
    for entry in items: 
        if entry['distance'] <= 100: #sends email if any of the dynamodb entries has a distance less than 100
            try:  # Provide the contents of the email.
                response = ses.send_email(
                    Destination={
                        'ToAddresses': ['kentaxu@yahoo.com'],
                    },
                    Message={
                        'Body': {
                            'Text': {
                                'Data': str(entry['stationID']) + " intruder alert!!!"
                            },
                        },
                        'Subject': {
                            'Data': 'Intruder Alert'
                        },
                    },
                    Source='kentaxu@gatech.edu'
                )
            # Display an error if something goes wrong.
            except ClientError as e:
                print(e.response['Error']['Message'])
            break #breaks out of for loop
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

