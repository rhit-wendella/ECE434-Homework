#!/usr/bin/env python3

# Luke Wendel 12/13/22

import Adafruit_BBIO.GPIO as GPIO
import time

# Set up the buttons
GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)
GPIO.setup("P9_19", GPIO.IN)

GPIO.cleanup()

# Determine the size of the grid
xMax = int(input("What would you like the width to be? (Integer or else it breaks) "))
yMax = int(input("What would you like the length to be? (Integer or else it breaks) "))

# Current position of the cursor
y = 0
x = 0

# Creating the etch-a-sketch grid space
grid = [[' ' for i in range(xMax)] for j in range (yMax)]

# Where the cursor is currently
grid[y][x] = '+'

# The instructions for the etch-a-sketch
print("Instructions:")
print("'r' is to move right")
print("'l' is to move left")
print("'u' is to move up")
print("'d' is to move down")
print("'q' is to quit the program")
input("Press enter to continue")

# Function to print the grid
def printGrid():
    xNumbers = [" "]
    yNumbers = []
    # Make a list for the x-axis
    for i in range(xMax):
        xNumbers.append(str(i))
    # Make a list for the y-axis
    for i in range(yMax):
        yNumbers.append(str(i))
    # Make the list so it won't print out commas or brackets
    xNumbersList = ' '.join(str(item) for item in xNumbers)
    print(xNumbersList)
    for i in range(yMax):
        # Make the grid so it doesn't print out commas or brackets
        areaNew = ' '.join(str(item) for item in grid[i])
        # Print one line of the grid
        print(yNumbers[i], areaNew)


# Print first grid
printGrid()

# Main Loop
while True:
    # Figure out what direction to go
    #answer = input("What direction would you likue? (u, d, l, r) ")
    
    # Mark spot that the player just left
    grid[y][x] = "*"
    # Up
    if GPIO.input("P9_11") == 1:
        y=y-1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        printGrid()
        time.sleep(0.2)
    # Down
    elif GPIO.input("P9_13") == 1:
        y=y+1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        printGrid()
        time.sleep(0.2)
    # Left
    elif GPIO.input("P9_17") == 1:
        x=x-1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        printGrid()
        time.sleep(0.2)
    # Right
    elif GPIO.input("P9_19") == 1:
        x=x+1
        x=x%xMax
        y=y%yMax
        grid[y][x] = "+"
        printGrid()
        time.sleep(0.2)
    # Quit
    #elif answer == "q":
    #    exit()
    # Just in case they print anything else
    #else:
     #   print("I don't quite understand")
    # Mod the position to make sure it can loop around the grid
    # Move cursor to current position
    
    # Print Grid
    
    

        


