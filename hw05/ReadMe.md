# Homework 4 ECE 434

## Makefille
I made a Makefile and put it in my HW05 folder.

## Install Kernel Tools
Had trouble installing kernel tools and was not able to do it.

## Kernel Modules
Ran all the examples that I needed to. Also edited the gpio_test.c file in order to set up LED to turn on with the buttons. 

## ADXL345 Accelerometer
I finished this section. Found a resource online that gave me code to read the accelerometer. The file is adxl345.py. You import this file in the Etch-a-Sketch.py and then call it and run it. It reads the axes and reports the x, y, and z data. Move the board around to move the LED on the Etch-a-Sketch.

## LED flashing at different rates
I modified the led.c code and made it so it ran two different threads with two different LEDs. They then did have a different blinking period.