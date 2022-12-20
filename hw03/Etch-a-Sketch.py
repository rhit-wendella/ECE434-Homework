#!/usr/bin/env python3

# Luke Wendel 12/13/22

import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

yMax = 8
xMax = 8

# Set up the buttons
GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)
GPIO.setup("P9_19", GPIO.IN)

GPIO.cleanup()

bus = smbus.SMBus(2)
matrix_address = 0x70
# set up the LED led_matrix
bus.write_byte_data(matrix_address, 0x21, 0)
bus.write_byte_data(matrix_address, 0x81, 0)
bus.write_byte_data(matrix_address, 0xe7, 0)

left = '1'
right = '2'
maxCount = '1000000'

def init(eQep):
    counterpath = '/dev/bone/counter/'+eQep+'/count0'
    with open(counterpath+'/ceiling', 'w') as f:
        f.write(maxCount)
    with open(counterpath+'/enable', 'w') as f:
        f.write('1')
    return open(counterpath+'/count', 'r')

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

f1 = init(left)
f2 = init(right)

# initial value
f1.seek(0)
f2.seek(0)
olddata = int(f1.read()[:-1])
data2 = int(f2.read()[:-1])

# knobs

while True:
  f1.seek(0)
  f2.seek(0)

  data = int(f1.read()[:-1])
  if data != olddata:
      if data > olddata:
          x+=1
          grid[y % yMax][x % xMax] = '*'
          led_update(grid)
      elif data < olddata:
          x-=1
          grid[y % yMax][x % xMax] = '*'
          led_update(grid)
      olddata = data

  data = int(f2.read()[:-1])
  if data != data2:
      if data > data2:
          y+=1
          grid[y % yMax][x % xMax] = '*'
          led_update(grid)
      elif data < data2:
          y-=1
          grid[y % yMax][x % xMax] = '*'
          led_update(grid)
      data2 = data
  time.sleep(.2)
    

        


