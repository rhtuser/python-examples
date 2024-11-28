#!/usr/bin/env python3
def main():
    print("I am a module. Import me.")

# Only export the greet function.
__all__ = ["greet"]

# Default greeting.
greeting = "Hello"
# Special greetings for our friends.
greetings = {
    "John": "It's been a long time",
    "Jane": "Oh, hey",
    "Tom": "Waaazzzaaaaa"
}

# Return a default greeting if the name is not set (or is an empty
# string), otherwise return a personalised greeting (if we recognise
# one of our friends), otherwise just return the default greeting.
def greet(name = ""):
    if not name:
        return greeting
    elif name in greetings.keys():
        return greetings[name]
    return greeting

if __name__ == "__main__":
    main()
