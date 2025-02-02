"""
Created on Sat Dec 16 19:55:39 2023

@author: Rohan Anil Yalamali
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # Create a card object
                created_card = Card(suit, rank)
                self.deck.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_one(self): 
        return self.deck.pop()
        
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
    
    def add_card(self,card):
        return self.cards.append(card)
        
class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
        self.total = self.total - self.bet

chip = Chips()

def take_bet():
    while True:
        try:
            ask_bet = int(input("How much are you willing to bet i.e 50 or 100: "))
            print('\n')
            if chip.total < ask_bet:
                print("You don't have enough chips")
                print('\n')
                print(f"Available chips: {chip.total}")
                print('\n')
                continue
            elif ask_bet not in [50,100]:
                print("Sorry invalid choice. choose either 50 or 100")
                print('\n')
                continue
        except:
            print('\n')
            print("That is not a number. Please enter a digit")
            print('\n')
            continue
        else:
            chip.bet = ask_bet
            print("Thank you for your bet")
            print('\n')
            break

def player_hit(test_deck, human_player):
    human_player.add_card(test_deck.deal_one())
    if human_player.cards[-1].value == 11:
        if human_player.value <= 10:
            human_player.cards[-1].value = 11
        else:
            human_player.cards[-1].value = 1
    human_player.value += human_player.cards[-1].value

def dealer_hit(test_deck, computer_dealer):
    computer_dealer.add_card(test_deck.deal_one())
    if computer_dealer.cards[-1].value == 11:
        if computer_dealer.value <= 10:
            computer_dealer.cards[-1].value = 11
        else:
            computer_dealer.cards[-1].value = 1
    computer_dealer.value += computer_dealer.cards[-1].value

def hit_or_stand(test_deck,human_player):
    global playing  # to control an upcoming while loop
    while playing not in ['hit','stand']:
        playing = input('Do you want to hit or stand: ')
        print('\n')
        if playing not in ['hit','stand']:
            print("Sorry, Invalid choice")
            print('\n')
    if playing == 'hit':
        player_hit(test_deck, human_player)
        playing = True
    else:
        playing = False
    return playing
        
def show_some(human_player,computer_dealer):
    for show_card in human_player.cards:
        print(f"Player's card: {show_card}")
    print(f"Player's card value: {human_player.value}")
    print('\n')
    print(f"Dealer's card: {computer_dealer.cards[0]}")
    print("Dealer's one card is hidden")
    print(f"Dealer's card value: {computer_dealer.cards[0].value}")
    print('\n')
    
def show_all(human_player,computer_dealer):
    for card_showtime in human_player.cards:
        print(f"Player's card: {card_showtime}")
    print(f"Player's card value: {human_player.value}")
    print('\n')
    for card_show_time in computer_dealer.cards:
        print(f"Dealer's card: {card_show_time}")
    print(f"Dealer's card value: {computer_dealer.value}")
    print('\n')
    
def player_busts():
    if human_player.value > 21:
        return True
    else:
        return False

def player_wins():
    if human_player.value == 21 or human_player.value > computer_dealer.value:
        return True
    else:
        return False

def dealer_busts():
    if computer_dealer.value > 21:
        return True
    else:
        return False
    
def dealer_wins():
    if computer_dealer.value == 21 or computer_dealer.value > human_player.value:
        return True
    else:
        return False
        
def tie():
    if (human_player.value == 21 and computer_dealer.value == 21) or (human_player.value == computer_dealer.value):
        return True
    else:
        return False
    
def replay():
    user = "wrong"
    while user not in ['Y','y','N','n']:
        user = input("Do you want to play the game again (Y/N): ")
        print('\n')
        if user not in ['Y','y','N','n']:
            print("Sorry, wrong choice")
            print('\n')
    if user == "Y" or user == "y":
        return True
    elif user == "N" or user == "n":
        return False
    
while True:
    print("Welcome to Blackjack card game")
    print('\n')

    # Create & shuffle the deck, deal two cards to each player
    test_deck = Deck()
    test_deck.shuffle()
    
    human_player = Hand()
    computer_dealer = Hand()
    
    # Inform Player of their chips total 
    print(f"Available chips: {chip.total}")
    print('\n')
    
    # Prompt the Player for their bet
    take_bet()
    
    player_hit(test_deck, human_player)
    player_hit(test_deck, human_player)
    
    dealer_hit(test_deck, computer_dealer)
    dealer_hit(test_deck, computer_dealer)
    
    # Show cards (but keep one dealer card hidden)
    show_some(human_player, computer_dealer)
    
    while playing:  # recall this variable from the hit_or_stand function
        
        # If player's hand reaches 21, break out of the loop
        if human_player.value == 21:
            playing = False
            break

        # Prompt for Player to Hit or Stand
        hit_or_stand(test_deck, human_player)
        
        # If player's hand reaches 21, break out of the loop
        if human_player.value == 21:
            playing = False
            break
        
        # If player's hand exceeds 21, run player_busts() and break out of the loop
        if player_busts():
            playing = False
            break
        
        # Show cards (but keep one dealer card hidden)
        show_some(human_player, computer_dealer)
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_busts() == False:
        while computer_dealer.value < 17:
            dealer_hit(test_deck, computer_dealer)

    # Run different winning scenarios
    if tie():
        chip.win_bet()
        print("It's a tie")
        print('\n')
        show_all(human_player, computer_dealer)
        
    elif player_busts():
        chip.lose_bet()
        print("Player got busted")
        print('\n')
        print("Dealer won")
        print('\n')
        show_all(human_player, computer_dealer)
    
    elif dealer_busts():
        chip.win_bet()
        print("Dealer got busted")
        print('\n')
        print("Player won")
        print('\n')
        show_all(human_player, computer_dealer)

    elif player_wins():
        chip.win_bet()
        print("Player won")
        print('\n')
        show_all(human_player, computer_dealer)

    elif dealer_wins():
        chip.lose_bet()
        print("Dealer won")
        print('\n')
        show_all(human_player, computer_dealer)

    # Inform Player of their chips total 
    print(f"Available chips: {chip.total}")
    print('\n')

    # If player doesn't have minimum chips to bet, break out of the loop
    if chip.total == 0:
        print("Sorry, you don't have enough chips to play another round")
        print('\n')
        break
    
    # Ask to play again
    if replay():
        playing = True
        continue
    else:
        break









