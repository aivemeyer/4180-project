### Issues Update Log
* Issues with RTOS and Serial connection with Pi
  * Fix: Removed RTOS  
* Problems with making touchpad method run on interrupts
  * Fix: Touchpad method called continusouly in main loop
* Unable to run website using Wifi chip with the rest of the code.
  * Fix: Had to remove website portion
  * Note: Website runs on its own (website.cpp) where it can change threshold values and armed state
* Unable to run Bluetooth at the same time with the alarm system
  * Fix: Removed Bluetooth portion   
