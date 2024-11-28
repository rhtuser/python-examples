#!/usr/bin/env python3
from person import Person
from guest import Guest
from friend import Friend

def main():
    print("I am a module. Import me.")

# Only export the greet function.
__all__ = ["greet"]

# Default greeting for .
greeting = "Good day"

# Return a default greeting if the name is not set (or is an empty
# string), otherwise return a greeting belonging to the class of
# person we encountered - either a personalised greeting for friends,
# or a general greeting for guests, or this module's conservative
# default for general persons.
def greet(someone = None):
    if not someone:
        return greeting + ", stranger!"
    elif isinstance(someone, Friend) or isinstance(someone, Guest):
        return someone.greeting + ", " + someone.name + "!"
    elif isinstance(someone, Person):
        return greeting + ", " + someone.name + "!"
    else:
        return greeting + ", " + someone + "!"

if __name__ == "__main__":
    main()
