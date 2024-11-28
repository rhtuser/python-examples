#!/usr/bin/env python3
class Person:
    def __init__(self, name):
        self._name = str(name).capitalize()

    # The "traditional" way of obtaining and setting attributes.
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = str(name).capitalize()

    # The "Pythonic" way of obtaining and setting attributes.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = str(name).capitalize()

    # Placeholder for a greeting.
    def greeting(self):
        pass

    # A convenient way of generating string representations of objects.
    def __str__(self):
        return "Person[Name: " + self._name + "]"

    # A test for equality - all attributes need the same values.
    def __eq__(self, obj):
        if type(obj) != Person:
            return False
        return self._name == obj.name

def main():
    print("This is a class module. Import it.")

if __name__ == "__main__":
    main()