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
    return "X" if random.randint(1, 2) == 1 else "O"


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


def player_choice(board):

    while True:
        response = int(input("What position do you want to play?"))
        if space_check(board, response) is False:
            return response


# player_choice(test_board)


def replay():
    while True:
        choice = input("Input Y or N to play again.")
        if choice == "Y":
            return True
        else:
            return False


def lets_play():
    test_board = ["#", "", "", "", "", "", "", "", "", ""]
    print("Welcome to Tic Tac Toe!")

    # Set the game up here
    # display_board(test_board)

    player1, player2 = player_input()
    print("Player1: " + player1, "Player 2: " + player2)
    active_player = choose_first()
    print("You go first, " + active_player)

    while True:

        # user chooses spot
        position_chosen = player_choice(test_board)
        # verify spot avail
        place_marker(active_player, test_board, position_chosen)
        print(test_board)
        print(display_board(test_board))
        if win_check(test_board, active_player):
            print(active_player+" You won!")
            break
        active_player = "X" if active_player == "O" else "O"
        # need to print out who's turn per

    # if want to play again game:
    if replay():
        lets_play()


lets_play()


