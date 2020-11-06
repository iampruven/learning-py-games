# Tic Tac Toe Game

# player1 = input("Please choose a marker: 'X' or 'O'")
# position = int(input('Please enter a number between 1-9:'))

from IPython.display import clear_output

def display_board(board):
    # create the set up of the board
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])

test_board = ['#','X','O','X','O','X','O','X','O','X']
# print(display_board(test_board))

def player_input():
    player1 = 'Wrong'

    while player1 not in ['X', 'O']:
        player1 = input('Player 1, Choose X or O as your character: ')

        if player1 not in ['X', 'O']:
            print('Select either X or O.')
    if player1 == 'X':
        player2='O'
    else:
        player2='X'
    return (player1, player2)
print(player_input())
# can use tuple unpacking
# player1_marker, player2_marker = player_input()

def place_marker(board, marker, position):
    choice = 'wrong'

    while choice not in ['1', '2', '3', '4', '5', '6', '7','8','9']:
        choice = input('Please select a value from 1-9, that has not been chosen yet. ')
        if choice not in ['1', '2', '3', '4', '5', '6', '7','8','9']: 
            print('Please select a proper value.')