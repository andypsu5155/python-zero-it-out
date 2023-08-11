from random import randint, shuffle

def set_card_name(card_num):
    if card_num == 1:
        return "ace"
    if card_num == 2:
        return "two"
    elif card_num == 3:
        return "three"
    elif card_num == 4:
        return "four"
    elif card_num == 5:
        return "five"
    elif card_num == 6:
        return "six"
    elif card_num == 7:
        return "seven"
    elif card_num == 8:
        return "eight"
    elif card_num == 9:
        return "nine"
    elif card_num == 10:
        return "ten"
    elif card_num == 11:
        return "jack"
    elif card_num == 12:
        return "queen"
    elif card_num == 13:
        return "king"

class Card():
    def __init__(self, card_num, card_type):
        self.card_num = card_num
        self.card_type = card_type
        self.card_name = set_card_name(card_num)
        self.face_down = True       # Ass up


card_deck = []
player_hand = []

def add_hearts(deck):
    i = 1
    while i < 14:
        deck.append(Card(i, "hearts"))
        i+=1
def add_clubs(deck):
    i = 1
    while i < 14:
        deck.append(Card(i, "clubs"))
        i += 1
def add_diamonds(deck):
    i = 1
    while i < 14:
        deck.append(Card(i, "diamonds"))
        i += 1
def add_spades(deck):
    i = 1
    while i < 14:
        deck.append(Card(i, "spades"))
        i += 1
def initialize_deck(deck):
    add_hearts(deck)
    add_clubs(deck)
    add_diamonds(deck)
    add_spades(deck)
    shuffle(deck)

def draw_card(deck, player_hand, num):
    i = 0
    while i < num:
        player_hand.append(deck[0])
        deck.remove(deck[0])
        i+=1

def print_cards(deck):
    for card in deck:
        print(str(card.card_name).title() + " of " + card.card_type)


initialize_deck(card_deck)
draw_card(card_deck, player_hand,5)

print_cards(player_hand)


