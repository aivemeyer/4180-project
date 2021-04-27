import sys, os
import time
import boto3

#Values for AWS credentials (change these based on user)
AWS_ACCESS_KEY="AKIASXPIV3TYQ2WTEYCV"
AWS_SECRET_ACCESS_KEY="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"
AWS_REGION="us-east-1"
DYNAMODB_TABLE='4180'
    
#Accesses dynamodb table 
dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name =AWS_REGION)

table = dynamodb.Table(DYNAMODB_TABLE)

table.put_item(
    Item={
        "stationID": "mbed1",           #creates stationID parameter for where the distance reading is coming from
        "timestamp": int(time.time()),  #creates timestamp for when the reading was made
        "distance": 5                   #distance sensor reads (currently dummy number)
        }
    )

print("test")