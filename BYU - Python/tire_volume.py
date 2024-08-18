import math
from datetime import datetime
current_date = datetime.now()

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = math.pi * width**2 * aspect *(width * aspect + 2540 * diameter)/10000000000

print(f'The date is: {current_date:%Y-%m-%d}')
print(f"The approximate volume is {v:.2f} liters")

with open("volumes.txt", "a") as file:
    file.write("{} {}, {}, {}, {:.2f}".format(current_date, width, aspect, diameter, v))