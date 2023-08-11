import pygame
from random import shuffle
pygame.font.init()

WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

CARD_SCALE = .2

FONT = pygame.font.SysFont('comicsans', 100)
scores = []

def set_card_name(card_num):
    if card_num == 1:
        return "ace"
    if card_num == 2:
        return "2"
    elif card_num == 3:
        return "3"
    elif card_num == 4:
        return "4"
    elif card_num == 5:
        return "5"
    elif card_num == 6:
        return "6"
    elif card_num == 7:
        return "7"
    elif card_num == 8:
        return "8"
    elif card_num == 9:
        return "9"
    elif card_num == 10:
        return "10"
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
        card_image = pygame.image.load("playing_cards/"+self.card_name+"_of_"+self.card_type+".png")
        self.image = pygame.transform.scale(card_image, (card_image.get_width()*CARD_SCALE, card_image.get_height()*CARD_SCALE))
        self.card_width = self.image.get_width()
        self.card_height = self.image.get_height()
        self.coord = []
        self.operation = ""

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

def set_card_coordinates(deck):
    x = 15
    for card in deck:
        card.coord = [x, 50]
        x += card.image.get_width() + 15

def display_cards(deck):
    for card in deck:
        WIN.blit(card.image, (card.coord[0], 50))

def display_selected_card(selection, deck):
    border_width = 7

    x = deck[selection-1].coord[0]-border_width
    y = deck[selection-1].coord[1]-border_width
    width = deck[selection-1].card_width + border_width*2
    height = deck[selection-1].card_height + border_width*2
    selected_rect = pygame.rect.Rect(x, y, width, height)
    pygame.draw.rect(WIN, YELLOW, selected_rect)

def change_card_operation(deck, selection, operation):
    deck[selection-1].operation = operation

def display_operation(deck):
    for card in deck:
        if(card.operation == "add"):
            text = FONT.render("+", 1, WHITE)
            x = card.coord[0]+card.card_width/2-text.get_width()/2
            y = card.coord[1]+card.card_height-30
            WIN.blit(text, (int(x), y, text.get_width(), text.get_height()))
        elif(card.operation == "subtract"):
            text = FONT.render("-", 1, WHITE)
            x = card.coord[0]+card.card_width/2-text.get_width()/2
            y = card.coord[1]+card.card_height-30
            WIN.blit(text, (int(x), y, text.get_width(), text.get_height()))

def compute_score(deck):
    result = 0
    for card in deck:
        if card.operation == "add":
            print(str(result) + " + " + str(card.card_num) + " = ")
            result += card.card_num
            print(result)
        else:
            print(str(result) + " - " + str(card.card_num) + " = ")
            result -= card.card_num
            print(result)
    return "Result = " + str(result)

def display_result(result):
    text = FONT.render(str(result), 1, WHITE)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 250, text.get_width(), text.get_height()))
    pygame.display.update()

def draw_window(deck, player_deck, selection, result):
    WIN.fill((200, 200, 200))

    display_selected_card(selection, player_deck)
    display_cards(player_deck)
    display_operation(player_deck)
    display_result(result)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    card_deck = []
    player_hand = []

    initialize_deck(card_deck)
    draw_card(card_deck, player_hand, 5)
    round = 1
    current_selection = 1
    result=""

    while run:
        clock.tick(FPS)
        i = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and current_selection<5:
                   current_selection+=1
                if event.key == pygame.K_a and current_selection>1:
                   current_selection-=1
                if event.key == pygame.K_w:
                    change_card_operation(player_hand, current_selection, "add")
                if event.key == pygame.K_s:
                    change_card_operation(player_hand, current_selection, "subtract")
                if event.key == pygame.K_RETURN:
                    result = compute_score(player_hand)
                    display_result(result)
                    scores.append(result)
                    print(scores)
                    pygame.time.delay(3000)
                    main()

        set_card_coordinates(player_hand)
        draw_window(card_deck, player_hand, current_selection, result)

    pygame.quit()




main()