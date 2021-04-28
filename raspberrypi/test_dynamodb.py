import sys, os
import time
import boto3

AWS_ACCESS_KEY="Enter Access Key Here"
AWS_SECRET_ACCESS_KEY="Enter Secret Access Key Here"
AWS_REGION="Enter region here"
DYNAMODB_TABLE='Enter Dynamodb table here'
    
#connects to dynamodb    
dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name =AWS_REGION)

table = dynamodb.Table(DYNAMODB_TABLE)

table.put_item(
    Item={
        "stationID": "mbed1",
        "timestamp": int(time.time()),
        "distance": 5 #sends value 5 to see if connection to dynamodb can be made
        }
    )

print("test")