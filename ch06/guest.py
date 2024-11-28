#!/usr/bin/env python3
from person import Person

class Guest(Person):
    _default_greeting = "Hello"

    # This is also called "constructor method" in some languages.
    def __init__(self, name):
        super().__init__(name)
        self._greeting = self._default_greeting

    # Persons can only use default greeting (i.e. we can't change it).
    @property
    def greeting(self):
        return self._greeting

    # A convenient way of generating string representations of objects.
    def __str__(self):
        return "Guest[" + super().__str__() + ", Greeting: " + self._greeting + "]"

    # A test for equality - all attributes need the same values.
    def __eq__(self, obj):
        if type(obj) != Guest:
            return False
        return self._name == obj.name and self._greeting == obj.greeting

def main():
    print("This is a class module. Import it.")

if __name__ == "__main__":
    main()
