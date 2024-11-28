#!/usr/bin/env python3
import random

def main():
    print("I am a module. Import me.")

# Only export the get_quote function.
__all__ = ["get_quote"]

# A tuple containing all the known quotes.
quotes = (
    "Flattery will go far tonight.",
    "He who laughs at himself never runs out of things to laugh at.",
    "He who laughs last is laughing at you.",
    "He who throws dirt is losing ground.",
    "Some men dream of fortunes, others dream of cookies.",
    "The greatest danger could be your stupidity.",
    "We don't know the future, but here's a cookie.",
    "The world may be your oyster, but it doesn't mean you'll get its pearl.",
    "You will be hungry again in one hour.",
    "The road to riches is paved with homework.",
    "You can always find happiness at work on Friday.",
    "Actions speak louder than fortune cookies.",
    "Because of your melodic nature, the moonlight never misses an appointment.",
    "Don't behave with cold manners.",
    "Don't forget you are always on our minds.",
    "Fortune not found? Abort, Retry, Ignore.",
    "Help! I am being held prisoner in a fortune cookie factory.",
    "It's about time I got out of that cookie.",
    "Never forget a friend. Especially if he owes you.",
    "Never wear your best pants when you go to fight for freedom."
)

# Return a random quote if the parameter is unset. If set, check that
# it is not too large, and return the quote under that number.
def get_quote(which = None):
    if not which and which != 0:
        return quotes[random.randint(0, len(quotes) - 1)]
    elif int(which) >= len(quotes):
        return "Quote is: number too large."
    return quotes[int(which)]

if __name__ == "__main__":
    main()
