import sys, os
import time
import boto3
import serial

#Values to access AWS
AWS_ACCESS_KEY="Enter Access Key Here"
AWS_SECRET_ACCESS_KEY="Enter Secret Access Key Here"
AWS_REGION="Enter region here"
DYNAMODB_TABLE='Enter Dynamodb table here'
    
#accesses dynamodb table on aws   
dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name =AWS_REGION)

table = dynamodb.Table(DYNAMODB_TABLE)

while(True):
    #gets value from mbed serial to pi
    device = serial.Serial('/dev/ttyACM0')
    data = str(device.readline())[2:-3]
    temp = data.split(',')

    #Sends sonar distance/threshold readings to dynamodb on AWS
    try:
        table.put_item(
            Item={
                "stationID": "mbed1",           #sends mbed1 as stationID to dynamodb
                "timestamp": int(time.time()),  #sends current time as timestamp
                "distance": temp[0],           #sends sonar reading from mbed through serial to dynamodb
                "threshold": temp[1]          #sends threshold value from mbed to dynamodb
                }
            )
    except:
        continue

    print("test")