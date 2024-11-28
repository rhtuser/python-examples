#!/usr/bin/env python3
from person import Person
from guest import Guest
from friend import Friend
import greetings

# For a specific set of objects, say hello.
not_an_object = "John Doe"
unknown = Person("Richard")
acquaintance = Guest("John")
friend = Friend("Tom")

print(greetings.greet())
print(greetings.greet(''))
print(greetings.greet(not_an_object))
print(greetings.greet(unknown))
print(greetings.greet(acquaintance))
print(greetings.greet(friend))
