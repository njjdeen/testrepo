# -*- coding: utf-8 -*-
"""

Blackjack game


"""

import random

#####create global variables

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


######Create classes

#Class representing a single card and its characteristics

class Card():
    

    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
        

#Now make a class that represents a Deck of cards
#Card class is adopted

class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
'''

# Player class, with characteristics

class Player():
    def __init__(self,name):
        self.name = name
        # a new player has no cards
        self.all_cards = []
        
    def remove_one(self):
        #removes one card from the top of the deck
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    
'''
    
#Class to keep track of the number of chips and bets

class Bankroll():
    
    def __init__(self,owner, balance):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'new balance: {self.balance}')
        
    def withdraw(self,amount):
        
        if amount > self.balance:
            print("Funds unavailable, bet was not placed!")
        else: 
            self.balance = self.balance - amount
      

#Class for the player's hand and its total value

class Hand():
    
    def __init__(self):
        
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        
        self.cards.append(card)
        self.value = self.value + card.value
        
    def adjust_for_ace(self):
        
        self.value = self.value - 10
        
  


#Function that allows player to place bets using user input

def take_bet(chips):
    
    
    enough_balance = False
    
    while enough_balance == False:
        while True:
            try:
                bet = int(input("please place your bet: "))
            except:
                print("please place an integer bet that does not exceed the current balance")
                continue
            else: 
                break
        
        if chips.balance < bet:
            print("Unsufficient chips, please place a lower bet")
            print(f"current balance: {chips.balance}")
            
        else:
            
            enough_balance = True
            chips.withdraw(bet)

    return bet


#function that gives player another card

def hit(deck, hand):
    
    card = deck.deal_one()
    
    hand.add_card(card)
    
    if hand.value > 21:
        
        if card.rank == 'Ace':
            
            hand.adjust_for_ace()
    

#Function that prompts player to hit or stand

def hit_or_stand(deck, hand):
    
    global playing
    
    choice = 'wrong'
    
    while choice not in ['H','S']:
        choice = input("HIT or STAND? (press H or S): ")

    if choice == 'H':
        
        hit(deck,hand)
    
    else:
        
        playing = False
        
    return

#function that shows all player's cards and one of the dealer

#input: dealers hand and players hand

def show_some(player,dealer):
    
    #show players full hand
    print("player's cards:")
    #print(len(player.cards))
    for card in range(len(player.cards)):
        
        print(player.cards[card])
    
    print(f'Value: {player.value} \n')
    
    
    #dealers card
    print("Dealer's Card:")
    print(dealer.cards[0])
    

    return


#Function that shows all cards from dealer and player

def show_all(player,dealer):

    #show players full hand
    print("player's cards:")
    
    for card in range(len(player.cards)):
        
        print(player.cards[card])
    
    print(f'Value: {player.value} \n')
    
    #dealers full hand
    print("Dealer's Cards:")
    
    for card in range(len(dealer.cards)):
        
        print(dealer.cards[card])
    
    print(f'Value: {dealer.value} \n')
    
    return

#Function that is activated when player busts

def player_busts(playerchips, bet):
    
        
    print("BUST!!!")
    print("The dealer wins!")
        
    #remove chips from player's chip account
    #playerchips.withdraw(bet)
        

#function that is activated when player wins

def player_wins(playerchips,bet):
    
    print("Player has won!!")
    
    #add 2 times the bet to the chip account
    playerchips.deposit(2*bet)
    
    return

def dealer_busts(playerchips, bet):
    
    print("BUST!!!")
    print("Player has won!!")
    
    playerchips.deposit(2*bet)
    
    return

#function that is activated when dealer wins
    
def dealer_wins(playerchips, bet):
    
    print("Dealer wins!")
    
    #playerchips.withdraw(bet)
        
####


##############game STARTS HERE#####################



##Create new card deck and shuffle the cards
game_on = True

#give player initial balance to play with
initial_balance = 100

#initialize player
chips = Bankroll('player1', initial_balance)

#Welcome message
print("WELCOME to Blackjack!")
print("\n")
print(f"number of chips: {chips.balance}")
while game_on:
    
    new_deck = Deck()
    
    new_deck.shuffle()
    
    #ask player for their bet
    
    #place bet
    bet = take_bet(chips)        
        
    #start with empty hand
    hand_dealer = Hand()
    hand_player = Hand()
    
    #Deal two cards to each player
    for i in range(2):
        hand_dealer.add_card(new_deck.deal_one())
        hand_player.add_card(new_deck.deal_one())
        
    
    show_some(hand_player,hand_dealer)
    
    playing = True
    player_has_busted = False
    while playing:
        
        
        
        hit_or_stand(new_deck,hand_player)
        
        print("\n"*100)
        
        show_some(hand_player,hand_dealer)
        
        if hand_player.value > 21:
            player_busts(chips,bet)
            print("\n")
            player_has_busted = True
            playing = False

    if player_has_busted == False:
        
        
        
        show_all(hand_player, hand_dealer)
        
        if hand_dealer.value >= 17:
            if hand_player.value > hand_dealer.value:
                player_wins(chips,bet)
            if hand_player.value <= hand_dealer.value:
                dealer_wins(chips,bet)
                
        elif hand_dealer.value < 17:
            if hand_player.value <= hand_dealer.value:
                dealer_wins(chips,bet)
            else:
                dealers_turn = True
                while dealers_turn:
                    hand_dealer.add_card(new_deck.deal_one())
                    
                    print("\n")
                    
                    show_all(hand_player,hand_dealer)
                    
                    if hand_dealer.value > 21:
                        
                        dealer_busts(chips, bet)
                        dealers_turn = False
                        
                    elif hand_dealer.value >= 17 and hand_dealer.value >= hand_player.value:
                        
                        dealer_wins(chips,bet)
                        dealers_turn = False
                        
                    elif hand_dealer.value >= 17 and hand_dealer.value < hand_player.value:
                        
                        player_wins(chips,bet)
                        dealers_turn = False
                        
                    else:
                        continue
           
    print(f"total number of chips: {chips.balance}")
    
    choice = 'wrong'
    
    while choice not in ['y', 'n']:
        choice = input("would you like to keep playing? (y or n): ")
        print("\n"*100)
    
    if choice == 'y':
        game_on = True
    else: 
        game_on = False
        print("Thanks for playing, see you next time!")
        
    
        
    if chips.balance == 0 and choice == 'y':
        print("Unfortunately, you don't have any more chips to play with. Better luck next time!")
        game_on = False
    
