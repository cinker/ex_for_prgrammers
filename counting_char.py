#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Author: cinker
Last Modified: 

Counting the Number of Characters

[Example Output]
​ 	What is the input string? Homer
​ 	Homer has 5 characters.

[Constraints]
Be sure the output contains the original string.
Use a single output statement to construct the output.
Use a built-in function of the programming language to 
determine the length of the string.

[Challenges]
If the user enters nothing, state that the user must enter 
something into the program.
Implement this program using a graphical user interface and 
update the character counter every time a key is pressed. 
If your language doesn’t have a particularly friendly GUI 
library, try doing this exercise with HTML and JavaScript instead.
"""
import re

input_str=""
while not input_str:
    input_str = input("What is the input string? ")
len_of_str = len(re.sub('\s+','',input_str))
print("{input_str} has {len_of_str} characters.".format(
    input_str=input_str, len_of_str=len_of_str))
