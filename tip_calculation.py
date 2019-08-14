#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Author: cinker
Last Modified: 
This is a tip calculation

[Constraints]
Enter the tip as a percentage. For example, a 15% tip would be entered as 15, 
not 0.15. Your program should handle the division.
Round fractions of a cent up to the next cent.

Ensure that the user can enter only numbers for the bill amount and the tip 
rate. If the user enters non-numeric values, display an appropriate message 
and exit the program.
"""

import numbers

def tip_calc(bill_amount, tip_perct):
    if isinstance(bill_amount, numbers.Number) and \
        isinstance(tip_perct, numbers.Number):
            bill_amount = float(bill_amount)
            tip_perct = float(tip_calc)/100
            tip_amount = bill_amount*tip_perct
            total_amount = bill_amount+tip_amount
            print("The tip is ${0}".format(tip_amount))
            print("The total is ${0}".format(total_amount))
            return (tip_amount, total_amount)
    else:
        print("Please enter a valid number for the bill amount.")

if __name__ == "__main__":
    bill_amount = input("What is the bill? ")
    tip_perct = input("Please input tip percentage: ")
    tip_calc(bill_amount, tip_perct)

