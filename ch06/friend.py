#!/usr/bin/env python3
from guest import Guest

class Friend(Guest):
    _default_greeting = "Hey"

    # This is also called "constructor method" in some languages.
    def __init__(self, name, greeting = _default_greeting):
        super().__init__(name)
        self._greeting = greeting

    # Friends can use any greeting.
    @property
    def greeting(self):
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        self._greeting = greeting

    # A convenient way of generating string representations of objects.
    def __str__(self):
        return "Friend[" + super().__str__() + ", Greeting: " + self._greeting + "]"

    # A test for equality - all attributes need the same values.
    def __eq__(self, obj):
        if not (type(obj) in [Friend, Guest]):
            return False
        return self._name == obj.name and self._greeting == obj.greeting

def main():
    print("This is a class module. Import it.")

if __name__ == "__main__":
    main()
