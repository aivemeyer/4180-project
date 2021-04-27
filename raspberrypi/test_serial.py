import serial
while True:
    device = serial.Serial('/dev/ttyACM0')
    data = int(str(device.readline())[2:-3]) #removes b' at beginning and \n' at end from distance reading passed in from mbed
    print(data)
    print(type(data))