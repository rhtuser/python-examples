#!/usr/bin/env python3
import random

target = random.randint(1, 100)
nguesses = 0
nattempts = 0

while True:
    nattempts += 1
    try:
        guess = int(input("Try to guess my number: "))
        assert guess <= 100, "Number is out of valid range (too high). Try again."
        assert guess > 0, "Number is out of valid range (too low). Try again."
    except ValueError:
        print("The number is not a valid integer. Try again.")
        continue
    except AssertionError as err:
        print(str(err))
        continue
    
    nguesses += 1
    if guess < target:
        print("{} is too low, try again.".format(guess))
    elif guess > target:
        print("{} is too high, try again.".format(guess))
    else:
        print("{} is the correct number! Congratulations!".format(guess))
        nguesses -= 1
        break
    
print("You managed to guess the number in {} attempts, of which {} were incorrect.".format(nattempts, nguesses))
