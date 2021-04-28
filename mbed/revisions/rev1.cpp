#include "mbed.h"
#include "rtos.h"
#include <mpr121.h>
#include "ultrasonic.h"


// Create the interrupt receiver object on pin 26
InterruptIn interrupt(p26);

// Setup the Serial to the PC for debugging
Serial pc(USBTX, USBRX);

// Setup the i2c bus on pins 28 and 27
I2C i2c(p9, p10);

// Setup the Mpr121:
// constructor(i2c object, i2c address of the mpr121)
Mpr121 mpr121(&i2c, Mpr121::ADD_VSS);

bool movement = false; //variables for states
bool armed = true;

//checks distance from sonar
 void dist(int distance)
{
    //code to execute when the distance has changed
    printf("Distance %d mm\r\n", distance);
    if(distance <=100){
        movement = true;
    }
}

ultrasonic mu(p6, p7, .1, 1, &dist);    //Set the trigger pin to p6 and the echo pin to p7
                                        //have updates every .1 seconds and a timeout after 1
                                        //second, and call dist when the distance changes

//For Testing purposes
DigitalOut led1(LED2);

int hold0,hold1,hold2,hold3 = 0; //signal variables for correct password

void fallInterrupt(){
    int key_code=0;
    int i=0;
    int value=mpr121.read(0x00);
    value +=mpr121.read(0x01)<<8;
    i=0;
    // Checks to see if the combination: 0486 has been pressed in that order in the pinpad
    for (i=0; i<12; i++) {
        if (((value>>i)&0x01)==1) key_code=i;
    }
    
    //Section makes sure the pinpad takes the values 0486 in that order, but other values can still be in between
    if ((key_code ==0) && (hold0 == 0) && (hold1 == 0)&& (hold2 == 0) && (hold3 == 0)){ //checks to see if the first value is 0
        hold0 =1;}    
    if ((key_code ==4) && (hold0 == 1) && (hold1 == 0)&& (hold2 == 0) && (hold3 == 0)){ //checks to see if the second value is 4
        hold1 =1;}
    if ((key_code ==8) && (hold0 == 1) && (hold1 == 1)&& (hold2 == 0) && (hold3 == 0)){ //checks to see if the third value is 8
        hold2 =1;}

    if ((key_code ==6) && (hold0 == 1) && (hold1 == 1)&& (hold2 == 1) && (hold3 == 0)){ //checks to see if the lasst value is 6
        hold3 =1;}
    
    //Section makes sure that no other values are pressed in between 0486
    
    if ((hold0 == 1) && (hold1 == 1)&& (hold2 == 1) && (hold3 == 1)) {
        led1 = 1; 
        armed = false;
    }
}

int main() {
    interrupt.fall(&fallInterrupt);
    interrupt.mode(PullUp);
    mu.startUpdates();//start measuring the distance
    while(1)
    {
        //Do something else here
        mu.checkDistance();     //call checkDistance() as much as possible, as this is where
                                //the class checks if dist needs to be called.
    }
}
