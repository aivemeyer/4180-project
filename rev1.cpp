#include "mbed.h"
#include "rtos.h"
#include "uLCD_4DGL.h" //


Thread thread; //
Thread thread2; //
Mutex stdio_mutex; //
PwmOut speaker(p21); //
uLCD_4DGL uLCD(p28,p27,p29); //
bool armed;
bool movement; 

void Speaker_Function() {
    int i;
    if (armed && movement) { 
        // sounds two-tone siren if there is movement while armed
        for (i=0; i<26; i=i+2) {
            speaker.period(1.0/969.0);
            speaker = float(i)/50.0;
            wait(.5);
            speaker.period(1.0/800.0);
            wait(.5);
        }    
    }
}

void LCD_status() {
    if (!armed) {
        stdio_mutex.lock();
        uLCD.text_string("DISARMED",1,14, FONT_7X8, 0x00FF00); //green font
        stdio_mutex.unlock();
        Thread::wait(500);
        
        stdio_mutex.lock();
        uLCD.text_string("DISARMED",1,14, FONT_7X8, 0x000000); //black font
        stdio_mutex.unlock();
        Thread::wait(500);
    } else if (armed && !movement) {
        stdio_mutex.lock();
        uLCD.text_string("ARMED - STAY AWAY",1,14, FONT_7X8, 0xFFFFFF); //white font
        stdio_mutex.unlock();
        Thread::wait(500);
        
        stdio_mutex.lock();
        uLCD.text_string("ARMED - STAY AWAY",1,14, FONT_7X8, 0x000000); //black font
        stdio_mutex.unlock();
        Thread::wait(500);
    } else {
        stdio_mutex.lock();
        uLCD.text_string("INTRUDER",1,14, FONT_7X8, 0xFF0000); //red font
        stdio_mutex.unlock();
        Thread::wait(100);
        
        stdio_mutex.lock();
        uLCD.text_string("INTRUDER",1,14, FONT_7X8, 0x000000); //black font
        stdio_mutex.unlock();
        Thread::wait(100);
    }
}

void Speaker_Thread(){
    while(true){
    Speaker_Function();
    Thread::wait(250);
    }
}

void LCD_thread() {
    while (true) {
    LCD_status();
    Thread::wait(250);    
    }   
}

int main() {
    while (1) {
        thread.start(Speaker_Thread);
        thread2.start(LCD_thread);
    }
}