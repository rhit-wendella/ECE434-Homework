#!/usr/bin/env python3

# Luke Wendel 12/13/22

import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
from flask import Flask, render_template
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




@app.route("/")
def index():
  # Make the template for the html
  ledRedSts = '0'
  templateData = { 'title': 'GPIO output Status!', 'ledRed': ledRedSts,}
  return render_template('index.html', **templateData)
	
@app.route("/<action>")
def action(action):
  # Variables for the etch-a-sketch
  global x
  global y
  global grid
  global xMax
  global yMax

  # Checks if the UP link on the html is clicked and moves the led on the matrix
  if action == "Up":
    y-=1
    x=x%xMax
    y=y%yMax
    grid[y][x] = "*"
    led_update(grid)
    time.sleep(0.2)
  # Checks if the DOWN link on the html is clicked and moves the led on the matrix
  if action == "Down":
    y+=1
    x=x%xMax
    y=y%yMax
    grid[y][x] = "*"
    led_update(grid)
    time.sleep(0.2)
  # Checks if the LEFT link on the html is clicked and moves the led on the matrix
  if action == "Left":
    x-=1
    x=x%xMax
    y=y%yMax
    grid[y][x] = "*"
    led_update(grid)
    time.sleep(0.2)
  # Checks if the RIGHT link on the html is clicked and moves the led on the matrix
  if action == "Right":
    x+=1
    x=x%xMax
    y=y%yMax
    grid[y][x] = "*"
    led_update(grid)
    time.sleep(0.2)
  # Checks if the CLEAR link on the html is clicked and clears the leds on the matrix
  if action == "Clear":
    y = 0
    x = 0
    grid = [[' ' for i in range(xMax)] for j in range(yMax)]
    x=x%xMax
    y=y%yMax
    grid[y][x] = "*"

    led_update(grid)
    time.sleep(0.2)

		     
  templateData = { 'action': action, }

  return render_template('index.html', **templateData)

# Runs the program on the host and port
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
    
    

        


