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
"""

def tip_calc(bill_amount, tip_perct):
    tip_amount = bill_amount*tip_perct
    total_amount = bill_amount+tip_amount
    print("The tip is ${0}".format(tip_amount))
    print("The total is ${0}".format(total_amount))
    return (tip_amount, total_amount)

if __name__ == "__main__":
    bill_amount = float(input("What is the bill? "))
    tip_perct = int(input("Please input tip percentage: "))/100
    tip_calc(bill_amount, tip_perct)

