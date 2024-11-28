#!/usr/bin/env python3

# NOTE: We will learn about this in the next chapter.
import random

# Card colours.
colours = ("Hearts", "Diamonds", "Spades", "Clubs")

# Card ranks.
# NOTE: Card numbers from 10 to 2 are simply appended to this tuple.
#       We will learn about the "for" expression in a later chapter.
ranks = ("Ace", "King", "Queen", "Jack") + tuple(num for num in range(10, 2, -1))

# Here are the functions we will use in the game.

def shuffle():
    """ Creates a new deck of cards, in random order.
        Returns: a list of (rank, colour) tuples for all possible combinations.
    """
    # NOTE: Another (nested) "for" expression called "comprehension";
    #       we will learn about those later, but this one creates a
    #       cartesian product of ranks and colours.
    deck = [(a, b) for a in ranks for b in colours]

    # Let's shuffle the deck thoroughly (twice).
    # NOTE: This is why the "import random" at the beginning.
    random.shuffle(deck)
    random.shuffle(deck)
    return deck

def deal(card_deck, num_cards = 5):
    """ Takes a specified number of cards off the top of the deck.
        Parameters:
        - card_deck is a list of (rank, colour) tuples
        - num_cards is the number of cards to deal
        Returns: num_cards elements of (rank, colour).
        TODO: What if num_cards is greater than remaining?
    """
    hand = []
    for x in range(num_cards):
        rank, colour = card_deck[0]
        # NOTE: The double parentheses here are necessary to let the
        #       function know that we are removing/appending a tuple,
        #       and not two scalar values (which would be a syntax
        #       error anyway, as the remove() and append() functions
        #       only accept a single parameter).
        card_deck.remove((rank, colour))
        hand.append((rank, colour))
    return hand

def show_hand(hand_of_cards, whose = "your"):
    """ Displays the hand, enumerating each card.
        Parameters:
        - hand_of_cards is the hand to show
        - whose is the owner of the card deck
        Returns: nothing.
    """
    print("Here is {whose} hand:".format(whose = whose))
    seq = 1
    # NOTE: Remember unpacking? This is a nice example of it.
    for rank, colour in hand_of_cards:
        print("{0}: {1} of {2}".format(seq, rank, colour))
        seq += 1

def change_cards(game_deck, hand_of_cards, how_many = 0):
    """ Replaces a specified number of cards in the hand with
        new ones from the deck by asking for cards the player
        wants to replace and removing them, then replacing all
        of them with new ones at the end.
        Parameters:
        - game_deck are the cards remaining in the game
        - hand_of_cards is the player's hand
        - how_many is the number of cards to replace
        Returns: the new hand of cards for the player.
    """
    print("Changing {0} cards.".format(how_many))
    for x in range(how_many):
        while True:
            card = input("Please enter the card number you want to change: ")
            # NOTE: Every time we ask for a card to remove, the list
            #       becomes shorter by one, so we must check that the
            #       number of the card being removed isn't too large.
            if (not card.isnumeric()) or (int(card) < 1) or (int(card) > len(hand_of_cards)):
                print("I need a number between 1 and {0}. Try again.".format(len(hand_of_cards)))
                continue
            # NOTE: The card number minus one is because lists are
            #       always numbered starting with zero, whereas we,
            #       humans, prefer to start counting at one.
            (d_rank, d_col) = hand_of_cards[int(card) - 1]
            hand_of_cards.remove((d_rank, d_col))
            # NOTE: We don't want to show the hand after the last
            #       removed card - it will be shown when the program
            #       returns from this function.
            if x < (how_many - 1):
                show_hand(hand_of_cards)
            break
    return hand_of_cards + deal(game_deck, how_many)

# Initialise the game.
deck = shuffle()

# Deal five cards to the player and show them.
player = deal(deck, 5)
show_hand(player)

# Repeat until the player decides not to change any more cards.
while True:
    nchange = 0

    # Repeat until the player correctly chooses how many cards they want to replace.
    while True:
        print()
        nchange = input("How many cards do you want to change (up to three)? ")
        if (not nchange.isnumeric()) or (int(nchange) > 3):
            print("I need a number between 0 and 3. Try again.")
            continue

        nchange = int(nchange)
        break

    # If there are no more cards to change, stop.
    if nchange == 0:
        break

    # Change cards if the player wants to.
    player = change_cards(deck, player, nchange)
    show_hand(player)
