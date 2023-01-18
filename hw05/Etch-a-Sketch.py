#!/usr/bin/env python3

# Luke Wendel 01/16/23

import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
from flask import Flask, render_template
from adxl345 import ADXL345
app = Flask(__name__)

yMax = 8
xMax = 8


bus = smbus.SMBus(2)
matrix_address = 0x70
# set up the LED led_matrix
time.sleep(0.5)
bus.write_byte_data(matrix_address, 0x21, 0)
time.sleep(0.5)
bus.write_byte_data(matrix_address, 0x81, 0)
time.sleep(0.5)
bus.write_byte_data(matrix_address, 0xe7, 0)
time.sleep(0.5)

# Run the Accelerometor helper file
adxl345 = ADXL345()


# Current position of the cursor
y = 0
x = 0

# Creating the etch-a-sketch grid space
grid = [[' ' for i in range(xMax)] for j in range (yMax)]


def led_update(grid):
    led_matrix = ["", "", "", "", "", "", "", ""]
    # binary for led led_matrix
    for i in range(len(grid)):
      for j in range(len(grid)):
        if grid[j][i] == '*':
          led_matrix[i] += '1'
        else:
          led_matrix[i] += '0'
    for i in range(len(led_matrix)):
      led_matrix[i] = int(led_matrix[i], 2)

    # make red
    block_data = []
    for i in range(len(led_matrix)):
      block_data.append(0)
      block_data.append(led_matrix[i])
    # write to the i2c bus
    bus.write_i2c_block_data(matrix_address, 0, block_data)

led_update(grid)




while True:
    # Figure out what direction to go
    
    grid[y][x] = "*"
    # Get the axes values from the accelerometer
    axes = adxl345.getAxes(True)
    # Up
    if axes['y'] < -0.1:
        y=y+1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        led_update(grid)
        time.sleep(0.2)
    # Down
    elif axes['y'] > 0.1:
        y=y-1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        led_update(grid)
        time.sleep(0.2)
    # Left
    elif axes['x'] < -0.1:
        x=x-1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        led_update(grid)
        time.sleep(0.2)
    # Right
    elif axes['x'] > 0.1:
        x=x+1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        led_update(grid)
        time.sleep(0.2)
    
    

        


