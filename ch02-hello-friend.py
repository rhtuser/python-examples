#!/usr/bin/env python3

# Ask the visitor about their name.
# NOTE: Immediate input sanitation is possible, because input()
#       always returns a string.
visitor = input("What is your name? ").capitalize()

# Do we know the visitor? Use a special greeting if we do.
#
# NOTE: This is a common idiom - we set a default value, and then
#       only adjust it for special cases. It works better than
#       adding an "else" clause at the end, because it is easier
#       to forget the "else" than to start with a sensible default.
greeting = "Hello"
if visitor == "John":
    greeting = "It's been a while"
elif visitor == "Jane":
    greeting = "Oh, hey"

# Display a greeting.
# NOTE: A slightly different version, using string operators rather
#       than format(). Ultimately a matter of convention and style,
#       format() does make it easier to read the string, but may be
#       a bit more difficult to read due to parameter assignments.
print(greeting + ", " + visitor + "!")

# What is their age?
age = input("What is your age, {name}? ".format(name = visitor))

# NOTE: This will avoid constant conversions to number wherever we
#       need to use the age variable, which is originally a string.
#       (Why is it a string?)
age = int(age)

# Is it the right John or Jane?
# NOTE: This is a simple example of compound conditions.
if (visitor == "John" and age != 37) or (visitor == "Jane" and age != 45):
    print("Oh, sorry, you are not the {name} I know.".format(name = visitor))

# How much to their next round anniversary?
round = 10 - (age % 10)

# Go up to 100 years in steps of 10 and tell how long before then.
# NOTE: Most while loops start like this: set up initial values and
#       then keep adjusting them upon each iteration:
next_age = round + age  # 1. set up initial values
while next_age <= 100:  # 2. set a completion condition
    print("In {x} years, you will be {age}.".format(x = (next_age - age), age = next_age))
    next_age += 10      # 3. update the value (note the operator here!)

# Also count down to, but with a for loop.
# NOTE: This loop could be written without the break and continue
#       statements, and it would be considered much better style,
#       but we are trying to demonstrate how to escape a loop or
#       skip a step.
#       (How would you change it to avoid break and continue?)
for past_age in range(age, 0, -1):
    # Stop below 18 years.
    if (past_age < 18):
        break
    # Skip ages that are not multiples of five.
    if (past_age % 5 != 0):
        continue
    print("{x} years ago, you were {age}.".format(x = (age - past_age), age = past_age))
