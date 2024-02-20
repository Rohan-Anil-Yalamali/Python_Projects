# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:36:17 2023

@author: Rohan Anil Yalamali
"""
import random

def diplay_board(board):
    print(board[1:4])
    print(board[4:7])
    print(board[7:10])

def players():
    player1 = 'wrong'
    while player1 not in ['X','O']:
        player1 = input("Player 1 choose your symbol (X or O): ")
        if player1 not in ['X','O']:
            print("sorry, Invalid choice")
    if player1 == "X":
        player2 = 'O'
    else:
        player2 = 'X'
    return player1,player2
    
def place_marker(board, marker):
    position = 'wrong'
    acceptable_range = range(1,10)
    within_range = False
    already_placed = False
    
    while position.isdigit() == False or within_range == False or already_placed == False:    
        position = input("enter your position (1-9): ")
        if position.isdigit() == False:
            print("it is not a digit")
        elif position.isdigit() == True:
            if int(position) in acceptable_range:
                within_range = True
                if board[int(position)] == 'X' or board[int(position)] == 'O':
                    print('Position already taken.Choose another position')
                    already_placed = False
                else:
                    already_placed = True
            else:
                print("you are out of the range i.e (0-9)")
                within_range = False
    board[int(position)] = marker
    
def win_check(board, mark):
    if list(mark*3) == board[1:4] or list(mark*3) == board[3:10:3] or list(mark*3) == board[1:8:3] or list(mark*3) == board[2:9:3] or list(mark*3) == board[1:10:4] or list(mark*3) == board[4:7:1] or list(mark*3) == board[3:8:2] or list(mark*3) == board[7:10:1]:
        return True
    else:
        return False
    
def choose_first():
    first = random.randint(1, 2)
    if first == 1:
        print("player1 will go first")
    else:
        print("player2 will go first")
    return first
    
def full_board_check(board):
    return "".join(board[1::]).isalpha()
        
def replay():
    user = "wrong"
    while user not in ['Y','y','N','n']:
        user = input("do you want to play the game again (Y/N): ")
        if user not in ['Y','y','N','n']:
            print("sorry, wrong choice")
    if user == "Y" or user == "y":
        return True
    elif user == "N" or user == "n":
        return False

print('Welcome to Tic Tac Toe!')

game_on = True

while True:
    board = ['0','1','2','3','4','5','6','7','8','9']
    player1,player2 = players()
    print(f'Player1:{player1}\nPlayer2:{player2}')
    first = choose_first()
    diplay_board(board)
    while game_on:
        #player1 turn
        if first == 1:
            print("Player 1 turn")
            print(f'Player1:{player1}\nPlayer2:{player2}')
            place_marker(board, player1)
            diplay_board(board)
            if win_check(board, player1):
                print("congratulations player 1 won the game")
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                break
            else:
                pass
            print("Player 2 turn")
            print(f'Player1:{player1}\nPlayer2:{player2}')
            place_marker(board, player2)
            diplay_board(board)
            if win_check(board, player2):
                print("congratulations player 2 won the game")
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                break
            else:
                pass
        else:
            #player2 turn
            print("Player 2 turn")
            print(f'Player1:{player1}\nPlayer2:{player2}')
            place_marker(board, player2)
            diplay_board(board)
            if win_check(board, player2):
                print("congratulations player 2 won the game")
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                break
            else:
                pass
            print("Player 1 turn")
            print(f'Player1:{player1}\nPlayer2:{player2}')
            place_marker(board, player1)
            diplay_board(board)
            if win_check(board, player1):
                print("congratulations player 1 won the game")
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                break
            else:
                pass
    if not replay():
        break
    
    
    
    

    
    
    
    
    
    