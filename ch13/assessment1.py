#!/usr/bin/env python3

string = """{nbottles} bottle{plural} of water on the wall!
{nbottles} bottle{plural} of water!
Take one down
And pass it around"""

plural = 's'

for nbottles in range(99, -1, -1):
    if nbottles == 1:
        plural = ''
    elif nbottles == 0:
        break
    print(string.format(nbottles = nbottles, plural = plural))

print("No more bottles of water on the wall!")
