#!/usr/bin/python

# Luke Wendel ECE434

import Adafruit_BBIO.GPIO as GPIO
import time

# Set up the LED
GPIO.setup("P8_11", GPIO.OUT)
GPIO.setup("P8_15", GPIO.OUT)
GPIO.setup("P8_17", GPIO.OUT)
GPIO.setup("P8_13", GPIO.OUT)
# Set up the buttons
GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)
GPIO.setup("P9_19", GPIO.IN)


GPIO.cleanup()


while True:
  #Light up the first LED
  if GPIO.input("P9_11") == 1:
    GPIO.output("P8_11", GPIO.HIGH)
  #Light up the second LED
  if GPIO.input("P9_13") == 1:
    GPIO.output("P8_15", GPIO.HIGH)
  #Light up the third LED
  if GPIO.input("P9_17") == 1:
    GPIO.output("P8_17", GPIO.HIGH)
  #Light up the fourth LED
  if GPIO.input("P9_19") == 1:
    GPIO.output("P8_13", GPIO.HIGH)
  #Let the LED shine for a bit
  time.sleep(0.25)
  #Turn off the LEDs
  GPIO.output("P8_11", GPIO.LOW)
  GPIO.output("P8_15", GPIO.LOW)
  GPIO.output("P8_17", GPIO.LOW)
  GPIO.output("P8_13", GPIO.LOW)