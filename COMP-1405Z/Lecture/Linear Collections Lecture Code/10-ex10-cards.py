#A deck of cards can be viewed as a list of cards, each of which can be described by a value and suit. Write a program to generate a deck of cards represented as a multi-dimensional list.

#How can you shuffle the deck of cards?
#How can you deal cards?
#How can you implement a simple card game (e.g., blackjack)?
import random

def shuffle(unshuffled):
    #take out a random card from unshuffled
    #add it into shuffled (initially an empty list)
    #repeat those steps until unshuffled is empty
    #return shuffled
    shuffled = []

    while len(unshuffled) > 0:
        card = unshuffled.pop(random.randint(0, len(unshuffled) - 1))
        shuffled.append(card)

    return shuffled

#simulate dealing num cards from adeck, return a new list containing the cards
def deal(adeck, num):
    result = []
    for i in range(num):
        if len(adeck) > 0:
            result.append(adeck.pop(0))
    return result


suits = ["C", "H", "D", "S"]
unshuffled = []
for suit in suits:
    for value in range(1, 14):
        card = [value, suit]
        unshuffled.append(card)

print("Unshuffled")
for card in unshuffled:
    print(card)

shuffled = shuffle(unshuffled)
print("Shuffled:")
for card in shuffled:
    print(card)
