""""
A manufacturing company needs a program that will help its employees 
pack manufactured items into boxes for shipping. 
Write a Python program named boxes.py that asks the user for two integers:
1.-the number of manufactured items
2.-the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. 
This must be a whole number. Note that the last box may be packed with fewer 
items than the other boxes.
"""
#so i can use the match.ceil function
import math
itemsnumber = int(input("Enter the number of items: "))
itemsbox = int(input("Enter the number of items per box: "))
#formula
boxes = math.ceil(itemsnumber / itemsbox)
print(f"For {itemsnumber} items, packing {itemsbox} items in each box, you wil need {boxes} boxes")