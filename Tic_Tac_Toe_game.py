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
        print('\n')
        if player1 not in ['X','O']:
            print('\n')
            print("Sorry, Invalid choice")
            print('\n')
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
        position = input("Enter your position (1-9): ")
        if position.isdigit() == False:
            print('\n')
            print("It is not a digit")
            print('\n')
        elif position.isdigit() == True:
            if int(position) in acceptable_range:
                within_range = True
                if board[int(position)] == 'X' or board[int(position)] == 'O':
                    print('\n')
                    print('Position already taken. Choose another position')
                    print('\n')
                    already_placed = False
                else:
                    already_placed = True
            else:
                print('\n')
                print("You are out of the range i.e. (0-9)")
                print('\n')
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
        print("Player 1 will go first")
    else:
        print("Player 2 will go first")
    return first
    
def full_board_check(board):
    return "".join(board[1::]).isalpha()
        
def replay():
    user = "wrong"
    while user not in ['Y','y','N','n']:
        user = input("Do you want to play the game again (Y/N): ")
        print('\n')
        if user not in ['Y','y','N','n']:
            print('\n')
            print("Sorry, wrong choice")
            print('\n')
    if user == "Y" or user == "y":
        return True
    elif user == "N" or user == "n":
        return False

print('Welcome to Tic Tac Toe!')
print('\n')

game_on = True

while True:
    board = ['0','1','2','3','4','5','6','7','8','9']
    player1,player2 = players()
    print(f'Player1:{player1}\nPlayer2:{player2}')
    print('\n')
    first = choose_first()
    print('\n')
    diplay_board(board)
    print('\n')
    while game_on:
        #player1 turn
        if first == 1:
            print("Player 1 turn")
            print('\n')
            print(f'Player1:{player1}\nPlayer2:{player2}')
            print('\n')
            place_marker(board, player1)
            print('\n')
            diplay_board(board)
            print('\n')
            if win_check(board, player1):
                print("Congratulations Player 1 won the game")
                print('\n')
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                print('\n')
                break
            else:
                pass
            print("Player 2 turn")
            print('\n')
            print(f'Player1:{player1}\nPlayer2:{player2}')
            print('\n')
            place_marker(board, player2)
            print('\n')
            diplay_board(board)
            print('\n')
            if win_check(board, player2):
                print("Congratulations Player 2 won the game")
                print('\n')
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                print('\n')
                break
            else:
                pass
        else:
            #player2 turn
            print("Player 2 turn")
            print('\n')
            print(f'Player1:{player1}\nPlayer2:{player2}')
            print('\n')
            place_marker(board, player2)
            print('\n')
            diplay_board(board)
            print('\n')
            if win_check(board, player2):
                print("Congratulations Player 2 won the game")
                print('\n')
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                print('\n')
                break
            else:
                pass
            print("Player 1 turn")
            print('\n')
            print(f'Player1:{player1}\nPlayer2:{player2}')
            print('\n')
            place_marker(board, player1)
            print('\n')
            diplay_board(board)
            print('\n')
            if win_check(board, player1):
                print("Congratulations Player 1 won the game")
                print('\n')
                break
            else:
                pass
            if full_board_check(board):
                print("It's a tie! The board is full. Play once again")
                print('\n')
                break
            else:
                pass
    if not replay():
        break
    
    
    
    

    
    
    
    
    
    
    