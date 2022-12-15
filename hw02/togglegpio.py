
#!/usr/bin/env python
# Toggle GPIO pin as fast as possible

#Luke Wendel ECE434

import Adafruit_BBIO.GPIO as GPIO
import time

# get commandline arguments
delay = input("Input delay in Seconds (Decimals allowed) ")


# Set up LED
GPIO.setup("P8_11", GPIO.OUT)

# Toggle LED pin to the delay
while True:
    GPIO.output("P8_11", GPIO.HIGH)
    time.sleep(delay)
    GPIO.output("P8_11", GPIO.LOW)
    