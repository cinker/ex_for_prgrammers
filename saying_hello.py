#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Author: cinker
Last Modified: 

Write a new version of the program without using any variables.
Write a version of the program that displays different greetings for different people.
"""
import random

print("Version 1")
print("Hello, "+input("​What is your name? ")+ ", nice to meet you!")

print("Version 2")
greetings = ['Hello, {name}', 'Nice meeting you, {name}']
name = input("​What is your name? ")
print(greetings[random.choice(range(len(greetings)))].format(name=name))
