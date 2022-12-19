#!/usr/bin/python

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(2)

# TMP101NA address, 0x49(73)
# Select configuration register, 0x01(1)
#		0x60(96)	Continous conversion, Comparator mode
#					Polarity Active low, 12-Bit Resolution
bus.write_byte_data(0x49, 0x01, 0x60)

time.sleep(0.5)

bus.write_byte_data(0x4a, 0x01, 0x60)

time.sleep(0.5)

# TMP101NA address, 0x49(73)
# Read data back from 0x00(0), 2 bytes
# cTemp MSB, cTemp LSB
data = bus.read_i2c_block_data(0x49, 0x00, 2)

data2 = bus.read_i2c_block_data(0x4a, 0x00, 2)

# Convert the data to 12-bits
cTemp = (data[0] * 256 + (data[1] & 0xF0)) / 16
if cTemp > 2047 :
	cTemp -= 4096
cTemp = cTemp * 0.0625
fTemp = cTemp * 1.8 + 32

cTemp2= (data2[0] * 256 + (data2[1] & 0xF0)) / 16
if cTemp2 > 2047 :
	cTemp2 -= 4096
cTemp2 = cTemp2 * 0.0625
fTemp2 = cTemp2 * 1.8 + 32

# Output data to screen
print("Temperature in Celsius is : %.2f C" %cTemp)
print("Temperature in Fahrenheit is : %.2f F" %fTemp)
print("Temperature in Celsius is : %.2f C" %cTemp2)
print("Temperature in Fahrenheit is : %.2f F" %fTemp2)