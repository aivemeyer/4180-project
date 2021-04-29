# 4180 Project - Security System
By Kenta Xu, Abi Ivemeyer, Nishalini Shanmugan, Seung Wook Jin
*<p align="center">![Our Entire Setup](https://github.com/aivemeyer/4180-project/blob/main/images/Final.jpg)<br/>
Figure 1. Our complete setup.</p><br/>*

*<p align="center">![Security System Architecture Diagram](https://github.com/aivemeyer/4180-project/blob/main/images/4180Diagram.JPG)<br/>
Figure 2. Architecture Diagram for Security System.</p><br/>*

## Overview
<p> Our project is a security system on a breadboard that will upload data to the cloud. When turned on, the system will be armed with a constant red light. When motion is detected, the alarm will go off and the light will blink, sending an email notification to the user. IT will continue going off until the passcode is correctly entered, in which the sound stops and the light dims. While the system is on, it will be connected to Amazon Web Services and send distance readings. </p>

## Components 
### Mbed LPC1768
*<p align="center">![mbed](https://github.com/aivemeyer/4180-project/blob/main/images/Mbed.jpg)<br/>
Figure 3. Mbed.</p><br/>*
[mbed Wiki](https://os.mbed.com/handbook/Homepage)
 
### Raspberry Pi 3
*<p align="center">![Raspberyy Pi](https://github.com/aivemeyer/4180-project/blob/main/images/Raspberry%20Pi.jpg)<br/>
Figure 4. Raspberry Pi 3.</p><br/>*
[Raspberry Pi 3 Wiki](http://raspberrypiwiki.com/Raspberry_Pi_3_Model_B_Plus)

### MPR121 Capacitive Touch Sensor 
*<p align="center">![Touchpad](https://github.com/aivemeyer/4180-project/blob/main/images/Touchpad.jpg)<br/>
Figure 5. Touchpad.</p><br/>*
[Touchpad Wiki](https://os.mbed.com/users/4180_1/notebook/mpr121-i2c-capacitive-touch-sensor/)

### Speaker and Class D Amp
*<p align="center">![Speaker](https://github.com/aivemeyer/4180-project/blob/main/images/Speaker.jpg)
Figure 5. Speaker.</p><br/>*
*<p align="center">![Amp](https://github.com/aivemeyer/4180-project/blob/main/images/Amp.jpg)<br/>
Figure 6. Class D amplifier.</p><br/>*
[Speaker and Class D Amp Wiki](https://os.mbed.com/users/4180_1/notebook/using-a-speaker-for-audio-output/)

### Pushbutton
*<p align="center">![Pushbutton](https://github.com/aivemeyer/4180-project/blob/main/images/Pushbutton.jpg)<br/>
Figure 7. Pushbutton.</p><br/>*
[Pushbutton Wiki](https://os.mbed.com/users/4180_1/notebook/pushbuttons/)

### HC-SR04 Sonar Sensor
*<p align="center">![Sonar](https://github.com/aivemeyer/4180-project/blob/main/images/Sonar.jpg)<br/>
Figure 8. Sonar motion sensor.</p><br/>*
[Sonar Motion Sensor Wiki](https://os.mbed.com/users/4180_1/notebook/using-the-hc-sr04-sonar-sensor/)

### LED
*<p align="center">![LED](https://github.com/aivemeyer/4180-project/blob/main/images/LED.jpg)<br/>
Figure 9. Red LED light.</p><br/>*
[LED Wiki](https://os.mbed.com/users/4180_1/notebook/rgb-leds/)

### uLCD-144-G2 Color LCD
*<p align="center">![LCD](https://github.com/aivemeyer/4180-project/blob/main/images/LCD.png)<br/>
Figure 10. uLCD.</p><br/>*
[uLCD Wiki](https://os.mbed.com/users/4180_1/notebook/ulcd-144-g2-128-by-128-color-lcd/)

### External 5V Source
*<p align="center">![5V Source](https://github.com/aivemeyer/4180-project/blob/main/images/5V.png)<br/>
Figure 11. External 5V source.</p><br/>*

## Connection
### Mbed LPC1768 Pin Connections
*<p align="center">![mbed Pin Connections](https://github.com/aivemeyer/4180-project/blob/main/images/mbed-pinout.png)<br/>
Figure 12. Mbed Pinout .</p><br/>*
As shown in figure 3, our mbed is grounded, and Vout is 3.3 V. Pin 9 of the mbed is connected to the SDA pin of the touchpad. Pin 10 is connected to the SCL pin of the touchpad. A 4.7k Ohm resistor is connected between both pins. Pin 13 is connected to TX of the bluetooth. Pin 14 is connected to RX of the bluetooth. Pin 17 is connected to the Trig Pin of the Sonar Motion Sensor. Pin 18 is connected to the Echo Pin of the Sonar Motion Sensor. Pin 21 is connected to a 4.7k Ohm resistor, which is limiting the current of a Red Led. Pin 22 is connected to the In+ pin of the Class D Audio Amplifier. Pin 26 is connected to IRQ of the Touchpad. Pin 27 is connected to RX of the uLCD. Pin 28 is connected to TX of the uLCD. 
 
### Raspberry Pi 3 Pin Connections
For the Raspberry Pi 3, the usb connects to the microusb on the mbed. The HDMI on the Raspberry Pi 3 connects to the monitor.  
 
### MPR121 Capacitive Touch Sensor Pin Connections
*<p align="center">![mbed Pin Connections](https://github.com/aivemeyer/4180-project/blob/main/images/touchpad-pinout.JPG)<br/>
Figure 13. Touchpad Pinout .</p><br/>*

### Speaker and Class D Audio Amplifier 
*<p align="center">![5V Source](https://github.com/aivemeyer/4180-project/blob/main/images/speaker-pinout.JPG)<br/>
Figure 14. Speaker Pinout.</p><br/>*

### Adafruit Bluefruit LE UART Friend 
*<p align="center">![5V Source](https://github.com/aivemeyer/4180-project/blob/main/images/bluetooth-pinout.JPG)<br/>
Figure 15. Bluetooth Pinout.</p><br/>*
For our project, we used pin 13 and pin 14, respectively instead of pin 27 and pin 28 on the bluetooth. 

### HC-SR04 Sonar Motion Sensor
*<p align="center">![5V Source](https://github.com/aivemeyer/4180-project/blob/main/images/sonar-pinout.JPG)<br/>
Figure 16. Sonar Motion Sensor Pinout.</p><br/>*
For our project, we used pin 17 and pin 18 on the mbed instead of pin 6 and pin 7. 

### LED
The shorter leg of the led is grounded. The longer leg is connected to a 4.7K Ohm resistor, which is connected to pin 21 on the mbed. 

### Pushbutton 
We are using three pushbuttons. One pushbutton is to rearm it once it is disarmed. The other two push buttons are to increase and decrease the threshold. The first pushbutton is grounded and connected to pin 23 on the mbed. The other two pushbuttons are grounded and connected to pin 24 and pin 25 on the mbed. 

### uLCD-144-G2 Color LCD Pin Connections
*<p align="center">![5V Source](https://github.com/aivemeyer/4180-project/blob/main/images/ulcd-pinout.JPG)<br/>
Figure 17. uLCD Pinout.</p><br/>*
For our project, we used pin 27 and pin 28 instead of pin 9 and pin 10 on the uLCD. 
 
## Software Setup
 
#### Raspberry Pi
 
<ol>
<li>Ready Raspberry Pi (3 or above recommended).</li>
<li>Make sure your Raspberry Pi has an Internet connection.</li>
<li>Pull this repository’s raspberrypi directory onto your Pi.</li>
<li>Enter your AWS access key, secret access key, region, and table name into main.py.</li>
<li>While the mbed is running, run the main.py script on your Pi.</li>
</ol>
 
#### Amazon Web Services
 
<ol>
<li>Create IAM Role for a Lambda Function and attach the policy for full access to DynamoDB.</li>
<li>Create a new DynamoDB table to store station ID (partition key), timestamp (sort key), and sonar distance readings in Python 3.38.</li>
<li>On AWS Simple Email Services, add and verify your email for sending and receiving the notifications </li>
<li>Create a new Lambda Function and attach the role created in step 1.</li>
<li>Download the main.py from this repository’s lambda directory.</li>
<li>Update the AWS access key, secret access key, region, and table name into main.py. </li>
<li>Upload the main.py’s code to the Lambda Function.</li>
<li>For the Lambda Function, create a CloudWatch Events trigger that is scheduled for every minute.</li>
</ol>
 
## Development Notes
 
### 2021.4.13
* Wired touchpad, sonar, LED, LCD, and WiFi SOC to the mbed.
* Programmed touchpad to go into disarmed state when 4-digit PIN is entered.
* Programmed sonar to print distances.
 
### 2021.4.15
* Wired speaker and audio amplifier.
* Created disarmed state, armed state, and intruder state.
* Programmed LCD to print one of three states at a time.
* Programmed speaker to go off as an alarm.
* Programmed everything in RTOS.
 
### 2021.4.20
* Programmed WiFi to run website that can be connected.
* Removed RTOS due to issues.
* Got everything working out of RTOS.
 
### 2021.4.22
* Set up Raspberry Pi 3.
* Created Python script for Pi to send data to AWS DynamoDB.
* Created Lambda Function to read DynamoDB entries and send email if data (distance) passes threshold.
 
### 2021.4.27
* Programmed mbed to send distance readings from sonar through serial to Raspberry Pi.
* Raspberry Pi sends distance data to AWS DynamoDB successfully.
 
### 2021.4.28
* Fixed bug in 4 pin code for touchpad
* Previously would disarm as long as pin is pressed in order with any digits in between
* Added pushbutton to rearm the system after it is disarmed
* Made alarm only sound when intruder is nearby and armed
 
### 2021.4.29
* Removed WiFi 
* Added 2 more pushbuttons feature to increment and decrement alarm threshold
* Updated setup photo
