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

def area_of_room(length_in_feet, width_in_feet):
    if isinstance(length_in_feet, numbers.Number) and isinstance(width_in_feet, numbers.Number):
        length_in_feet=float(length_in_feet)
        width_in_feet=float(width_in_feet)
        print("You entered dimensions of {length_in_feet} feet by {width_in_feet} feet.".format(width_in_feet=width_in_feet, length_in_feet=length_in_feet))
    else:
        print("Please enter a valid number for the bill amount.")

if __name__ == "__main__":
    length_in_feet = input("What is the length of the room in feet? ")
    width_in_feet = input("What is the width of the room in feet? ")
    area_of_room(length_in_feet, width_in_feet)
