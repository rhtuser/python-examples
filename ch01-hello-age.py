#!/usr/bin/env python3

# Ask the visitor about their name.
visitor = input("What is your name? ")

# Capitalize the visitor's name, just in case.
# NOTE: Why does this work?
#       Why does it not work without an assignment?
visitor = visitor.capitalize()

# Display a greeting.
print("Hello, {name}!".format(name = visitor))

# What is their age?
age = input("What is your age, {name}? ".format(name = visitor))

# How much to their next round anniversary?
# NOTE: Why the int() around "age"?
round = 10 - (int(age) % 10)
print("So in {x} years you will be {age}!".format(x = round, age = (round + int(age))))

# Just a little conversion to hexadecimal.
print("In hexadecimal, that is {hexage}.".format(hexage = hex((round + int(age)))))
