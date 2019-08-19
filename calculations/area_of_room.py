#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Author: cinker
Last Modified: 
Create a program that calculates the area of a room. Prompt the user for 
the length and width of the room in feet. Then display the area in both square feet and square meters.

​ 	What is the length of the room in feet? 15
​ 	What is the width of the room in feet? 20
​ 	You entered dimensions of 15 feet by 20 feet.
​ 	The area is
​ 	300 square feet
​ 	27.871 square meters
"""
import numbers
import math

CONVERSION_RATIO=0.09290304

def area_of_room(length_in_feet, width_in_feet):
    try:
        length_in_feet=int(length_in_feet)
        width_in_feet=int(width_in_feet)
        area_by_feet = length_in_feet * width_in_feet
        area_by_sm = area_by_feet*CONVERSION_RATIO
        print("You entered dimensions of {length_in_feet} feet by {width_in_feet} feet.".format(width_in_feet=width_in_feet, length_in_feet=length_in_feet))
        print("The area is")
        print("{area_by_feet} square feet".format(area_by_feet=area_by_feet))
        print("{area_by_sm:.3f} square feet".format(area_by_sm=area_by_sm))
    except:
        print("Please enter a valid number.")

if __name__ == "__main__":
    length_in_feet = input("What is the length of the room in feet? ")
    width_in_feet = input("What is the width of the room in feet? ")
    area_of_room(length_in_feet, width_in_feet)
