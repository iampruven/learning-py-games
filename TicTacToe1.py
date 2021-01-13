# from IPython.display import clear_output
import random


def display_board(board):
    # create the set up of the board
    # clear_output()
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])


test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", ""]


def player_input():

    valid_response = False
    while valid_response is False:
        player1 = input("Player 1, do you want to represent X or O ?:")
        if player1 in ["X", "O"]:
            valid_response = True
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return (player1, player2)


def place_marker(marker, board, position):

    board[position] = marker


def win_check(board, mark):
    # vertical win
    if (
        (board[1] == mark and board[2] == mark and board[3] == mark)
        or (board[4] == mark and board[5] == mark and board[6] == mark)
        or (board[7] == mark and board[7] == mark and board[9] == mark)
    ):
        return True
    # horizontal win
    elif (
        (board[1] == mark and board[4] == mark and board[7] == mark)
        or (board[2] == mark and board[5] == mark and board[8] == mark)
        or (board[3] == mark and board[6] == mark and board[9] == mark)
    ):
        return True
    # diagonal win
    elif (board[1] == mark and board[5] == mark and board[9] == mark) or (
        board[3] == mark and board[5] == mark and board[7] == mark
    ):
        return True
    # did not win
    else:
        return False


def choose_first():
    return random.randint(1, 2)


def space_check(board, position):

    if board[position] in ["X", "O"]:
        return True
    else:
        return False


def full_board_check(board):
    for value in board:
        print(value)
        if value not in ["#", "X", "O"]:
            return False
    return True


# Not sure!
def player_choice(board):

    while True:
        response = int(input("What position do you want to play next?"))
        if space_check(board, response) is False:
            return response


# player_choice(test_board)


def replay():
    while True:
        choice = input("Input Y or N to play again.")
        if choice == "Y":
            return True


# print(replay())
# print(full_board_check(test_board))
# print(space_check(test_board,9))
# print(choose_first())
# print(win_check(test_board, 'O'))
# place_marker('X', test_board, 8)
# display_board(test_board)
