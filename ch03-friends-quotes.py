#!/usr/bin/env python3

# NOTE: It is a good practice to place all data definitions, such as
#       default values, or in this case, data sets, at the beginning
#       of the program (or, as we will see later, the function that
#       uses the data). This way it is easy to find them and change
#       them. Usually there is also a comment at the end of such a
#       section that clearly tells the reader where the code starts.
#       (see below)

# General greeting.
greeting = "Hello"

# How do we greet some of our known friends?
greetings = {
    "John": "It's been a long time",
    "Jane": "Oh, hey",
    "Tom": "Waaazzzaaaaa"
}

# Some random quotes:
# NOTE: This is a tuple. We will not be modifying it during execution.
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

# XXX END OF DEFINITIONS, ONLY CODE BELOW THIS LINE XXX

# Ask the visitor about their name.
visitor = input("What is your name? ").capitalize()

# Use a special greeting if a known friend popped by.
if visitor in greetings.keys():
    greeting = greetings[visitor]

# Greet the visitor.
print("{greet}, {person}!".format(greet = greeting, person = visitor))

# Ask which quote the visitor wants.
# NOTE: While endless loops such as this one are generally considered
#       unsafe and best avoided, in cases such as this they are a
#       great way of avoiding an increase in complexity of the code,
#       provided we are careful enough to ensure the loop will
#       eventually complete.
#       If we wanted to rewrite this section without an endless loop,
#       we would have to start with a false premise (such as setting
#       the "nquote" variable to something out of bounds (-1) before
#       entering the loop, and there would have to be a big condition
#       clause in the "while" statement, checking every possible
#       successful completion criterion.
#       This would inevitably lead to repeated conditions (once in
#       the "while" statement, and then once more within the loop
#       body, where problems are reported to the visitor), thus
#       making the code less readable, and more importantly, more
#       difficult and error-prone to maintain.
while True:
    nquote = input("I have {num} quotes for you, which one do you want, {name}? "
                    .format(num = len(quotes), name = visitor))

    # NOTE: Input sanitation is the most important thing in a program.
    #       This is why we must make sure the visitor entered a number,
    #       and that the number is within the bounds of the size of our
    #       quote list.
    if not nquote.isnumeric():
        print("Sorry, {num} is not a number. Try again.".format(num = nquote))
        continue
    elif int(nquote) > len(quotes):
        print("Sorry, I don't have that many quotes. Try again.")
        continue

    break

print(quotes[int(nquote) - 1])