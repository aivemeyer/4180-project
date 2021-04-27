import sys, os
import time
import boto3
import serial

#Values to access AWS
AWS_ACCESS_KEY="AKIASXPIV3TYQ2WTEYCV"
AWS_SECRET_ACCESS_KEY="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"
AWS_REGION="us-east-1"
DYNAMODB_TABLE='4180'
    
#accesses dynamodb table on aws   
dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name =AWS_REGION)

table = dynamodb.Table(DYNAMODB_TABLE)

while(True):
    #gets value from mbed serial to pi
    device = serial.Serial('/dev/ttyACM0')
    data = int(str(device.readline())[2:-3])

    #Sends sonar distance readings to dynamodb on AWS
    table.put_item(
        Item={
            "stationID": "mbed1",           #sends mbed1 as stationID to dynamodb
            "timestamp": int(time.time()),  #sends current time as timestamp
            "distance (mm)": data           #sends sonar reading from mbed through serial to dynamodb
            }
        )

    print("test")