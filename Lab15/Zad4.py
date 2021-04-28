class Card():
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Karo", "Wino", "Kier", "Trefl"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand():

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hand, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Ni ma karteluszek, ni ma grania")


def cardvalue(cr):
    if cr == "A":
        value = 1
    elif cr == "2":
        value = 2
    elif cr == "3":
        value = 3
    elif cr == "4":
        value = 4
    elif cr == "5":
        value = 5
    elif cr == "6":
        value = 6
    elif cr == "7":
        value = 7
    elif cr == "8":
        value = 8
    elif cr == "9":
        value = 9
    elif cr == "10":
        value = 10
    elif cr == "J":
        value = 11
    elif cr == "Q":
        value = 12
    elif cr == "K":
        value = 13
    else:
        value = 0
    return value


deck1 = Deck()
deck1.populate()
deck1.shuffle()
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand=1)

print("\n   Moja ręka:", my_hand)
print("Twoja ręka:", your_hand)

myval = cardvalue(my_hand.cards[0].rank)
yourval = cardvalue(your_hand.cards[0].rank)

if myval > yourval:
    print("\nJa wygrałem")
else:
    print("\nTy wygrałeś")
