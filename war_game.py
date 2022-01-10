'''

War Card game


'''

import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


##########Create Classes##########

#first make class for Card

class Card():
    

    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
        

#Now make a class that represents a Deck of cards

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
    
    
#Class that represetns the player

    
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
    
###################################################################

####   Setup the game

new_deck = Deck()

new_deck.shuffle()

player_one = Player('One')
player_two = Player("Two")


#split deck between players

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


### play the game
game_on = True


round_num = 0
while game_on:
    round_num = round_num + 1
    
    print(f"Round {round_num}")
    
    #check if any player has ran out of cards
    
    if len(player_one.all_cards) == 0:
        print("Player 1 is out of cards! Game Over")
        print("Player 2 wins!")
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print("Player 2 is out of cards! Game Over")
        print("Player 1 wins!")
        game_on = False
        break
    
    #put cards on the table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:
        
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            #then player one gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False #time for next round
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            #Then player two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
    
            at_war = False #time for next round
            
        else:
            print("WAR!")
            
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
    
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    