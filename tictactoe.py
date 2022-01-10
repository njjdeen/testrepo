import numpy as np
import random
import time

#Function that displays the board

test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    
    #this function takes in a 9-element long list and uses this to draw the
    #tic-tac-toe board
        
    
    print(" " + board[0] + " | " + board[1] +" | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] +" | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] +" | " + board[8])

    
    return

#display_board(test_board)


############function that asks player one to choose character

def player_input():
    
    marker1 = 'False'
    
    while marker1 not in ['X', 'O']:
    

        marker1 = input("Player 1, please choose your marker ('X' or 'O'): ")
        
        if marker1 not in ['X', 'O']:
            print('\n'*100)
            print("Sorry, the choice you made is not an option, please choose 'X' or 'O'")
    
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = "X"
    
    return marker1, marker2



### write function to decide which player goes first

def choose_first():
    
    print("Now it's time to decide which player gets the first turn")
    time.sleep(1.25)
    print("Flipping a coin.....")
    time.sleep(1.25)
    print("let me check..")
    print("\n")
    time.sleep(1)
    num = random.random()
    
    if num > 0.5:
        print("Player 1 gets to go first, goodluck!")
        return 'Player1'
        
    else:
        print("Player 2 gets to go first, goodluck!")
        return 'Player2'
    

#####function that allows player to choose a spot

def player_choice(board):
    
    
    within_range = False
    free_space = False

    while within_range == False or free_space == False:
        
        display_board(board)
        choice = input("please choose a free position to place your next marker (using 1-9):")
        choice = int(choice)
        
        if choice not in range(1,10):
            
            print("\nchoice not within range 1-9, please pick a space: \n")
            
            print("positions:")
            print(" 1 | 2 | 3")
            print("-----------")
            print(" 4 | 5 | 6")    
            print("-----------")
            print(" 7 | 8 | 9\n")
            
            #print("current board:")
            #display_board(board)
            continue
        else:
            within_range = True
        
        if space_check(board,choice) == False:
            print("space already taken, please pick another one:\n")
            
            print("positions:")
            print(" 1 | 2 | 3")
            print("-----------")
            print(" 4 | 5 | 6")    
            print("-----------")
            print(" 7 | 8 | 9\n")
            
            #print("current board:")
            #display_board(board)
            continue
        else:
            free_space = True
            
    return choice

        
    

#####function that checks if space on board is freely available

def space_check(board, position):
    
    
    
    if board[position-1] == " ":
        spacefree = True
    else:
        spacefree = False
        
    
    return spacefree
    
    
####function that checks if the board is full

def full_board_check(board):
    
    if " " in board:
        return False
    else:
        return True
    



###################function that places marker

#arguments: current board, marker, desired position
def place_marker(board, marker, position):
    
    board[position-1] = marker
    
    return board
    
    
#test place marker using test board
# =============================================================================
# place_marker(test_board,'$',8)
# display_board(test_board)
# =============================================================================

#### write function that checks if player has won

def win_check(board, marker):
    
    Win = False
    
    #find marker positions on the board
    marker_pos = set(np.where(np.array(board) == marker)[0])
    
    #marker_pos = marker_pos.sort()
    
    #print(marker_pos)
    
    
# =============================================================================
#     if [0,1,2] in marker_pos or marker_pos == [3,4,5] or marker_pos == [6,7,8] \
#         or marker_pos == [0,3,6] or marker_pos == [1,4,7] or marker_pos == [2,5,8] \
#             or marker_pos == [0,4,8] or [2,4,6] in marker_pos:
#         Win = True
# =============================================================================

    if {0,1,2}.issubset(marker_pos) or {3,4,5}.issubset(marker_pos) or \
        {6,7,8}.issubset(marker_pos) or {0,3,6}.issubset(marker_pos) or \
            {1,4,7}.issubset(marker_pos) or {2,5,8}.issubset(marker_pos) or \
                {0,4,8}.issubset(marker_pos) or {2,4,6}.issubset(marker_pos):
        Win = True
    
   
    return Win


######Function that asks player if he wants to play again
def replay():
    
    yesorno = "WRongchoice"
    
    while yesorno not in ["y", "n", "Y", "N"]:
    
        yesorno = input("Would you like a rematch? (Y or N)")
        
        if yesorno not in ["y", "n", "Y", "N"]:
            
            print("I don't understand, would you like to play again? (Y or N)")
            
    if yesorno == 'y' or yesorno == 'Y':
        return True
    else:
        return False
    

#test = win_check(test_board,'O')








############################################Start game#####################



game_on = True

while game_on:
    
    print("Welcome To Tic-Tac-Toe!!! \nLet's start with a nice and clean board to play our game..")

    clean_board = [" ", " ", " ", " ", " "," ", " ", " ", " "]

    board = clean_board

    time.sleep(2)
    print("\n \n")
    display_board(clean_board)
    print("There we go, game on!.")
    time.sleep(4)
    print("\n" * 1000)
    
    print("First, it's time to choose your markers")
    
    [marker1, marker2] = player_input()
    
    print('\n' * 100)
    
    print("allright, so player 1 will be '" + marker1 + "' and player 2 will be '" + marker2 + "'")
    time.sleep(2)
    print("\n" * 100)
    
    #decide which player gets to go first
    
    first_player = choose_first()
    time.sleep(3)
    print("\n" * 100)
    
    if first_player == "Player1":
        first_marker = marker1
        second_marker = marker2
        second_player = "Player2"
    else:
        first_marker = marker2
        second_marker = marker1
        second_player = "Player1"
    
    
    boardfull = False
    playerwin1 = False
    playerwin2 = False    
    while boardfull == False and playerwin1 == False and playerwin2 == False:
        
        #turn for both players
        print("\n"*20)
        print("Current Turn: " + first_player)
        
        
        position = player_choice(board)
        board = place_marker(board,first_marker,position)
        
        #check if board is full or a player has won
        boardfull = full_board_check(board)
        playerwin1 = win_check(board,marker1)
        playerwin2 = win_check(board,marker2)
        
        if boardfull:
            print("The board is full!")
            time.sleep(2)
            break
        
        if playerwin1:
            print("Player 1 has won the game!")
            break
            
        if playerwin2:
            print("Player 2 has won the game!")
            break
        
        print("\n"*20)
        print("Current Turn: " + second_player)
        
        position = player_choice(board)
        board = place_marker(board,second_marker,position)
        
        #check if board is full or a player has won
        boardfull = full_board_check(board)
        playerwin1 = win_check(board,marker1)
        playerwin2 = win_check(board,marker2)

        
        
        if boardfull:
            print("The board is full!")
            time.sleep(2)
        
        if playerwin1:
            print("Player 1 has won the game!")
            
        if playerwin2:
            print("Player 2 has won the game!")
    
    
    time.sleep(2)
    print("\n" * 8)
    
    game_on = replay()
    
print("Thanks for playing!! Shutting down...")
time.sleep(2)
