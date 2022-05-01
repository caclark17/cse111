# Write a Python program that reads from the keyboard the three numbers for a tire
# and computes and outputs the volume of space inside that tire
# First number is the width of the tire in millimeters
# Second number is the aspect ratio
# Third number in the diamter of inches of the wheel that the tire fits

import math

# Get the width, aspect ratio, and diameter from the user
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

# Compute the volume of the space inside a tire
parenthesis = (width * aspect_ratio) + (2540 * diameter)
width_squared = width ** 2
top = math.pi * width_squared * aspect_ratio * parenthesis
volume = top / 10000000000

print(f'The approximate volume is {volume:.2f}')

#Get current date from the computer's OS
from datetime import datetime

# Opens a text file named volumes.txt for appending.
with open("volumes.txt", "at") as volumes_file:

# Appends to the end of the volumes.txt file one line of text that contains the following five values:
# current date
# width of the tire
# aspect ratio of the tire
# diameter of the wheel
# volume of the tire

  current_date_and_time = datetime.now()
  print(f'{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}', file = volumes_file)
