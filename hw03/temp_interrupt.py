#!/usr/bin/env python
# Luke Wendel ECE434 12/19/22

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

# Initialize the I2C bus
bus = smbus.SMBus(2)

# Set up GPIO Pins for alert
GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)

GPIO.cleanup()
thigh = 25
tlow = 23
# Set up the sensors
bus.write_byte_data(0x49, 0x01, 0x60)
bus.write_byte_data(0x49, 0x02, tlow) # LOW TEMP LIMIT
bus.write_byte_data(0x49, 0x03, thigh)  # LOW TEMP LIMIT

bus.write_byte_data(0x4a, 0x01, 0x60)
bus.write_byte_data(0x4a, 0x02, tlow)  # LOW TEMP LIMIT
bus.write_byte_data(0x4a, 0x03, thigh)  # HIGH TEMP LIMIT

while True:
    # Check for alerts on the GPIO lines
    if GPIO.input("P9_11") == 0:
        # Alert on P9_11
        data = bus.read_i2c_block_data(0x49, 0x00, 2)
        cTemp = (data[0] * 256 + (data[1] & 0xF0)) / 16
        if cTemp > 2047 :
            cTemp -= 4096
        cTemp = cTemp * 0.0625
        fTemp = cTemp * 1.8 + 32
        print("ALERT: Temperature in Celsius is : %.2f C" %cTemp)
        print("ALERT: Temperature in Fahrenheit is : %.2f F" %fTemp)
    if GPIO.input("P9_13") == 0:
        # Alert on P9_13
        data2 = bus.read_i2c_block_data(0x4a, 0x00, 2)
        cTemp2 = (data2[0] * 256 + (data2[1] & 0xF0)) / 16
        if cTemp2 > 2047 :
            cTemp2 -= 4096
        cTemp2 = cTemp2 * 0.0625
        fTemp2 = cTemp2 * 1.8 + 32
        print("ALERT 2: Temperature in Celsius is : %.2f C" %cTemp2)
        print("ALERT 2: Temperature in Fahrenheit is : %.2f F" %fTemp2)
    time.sleep(1)