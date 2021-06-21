# we gonna need a board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_is_on = True

#check if win or tie?
winner = None

# who's turn is it?
curr_player = "X"

# we need to display the board
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "      1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "      4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "      7 | 8 | 9")
    print("\n")

# play a game of tic-tac-toe
def play_game():

    #display initial board
    display_board()

    #we need to play until somebody wins or ties.
    while game_is_on:

        #handle single turn of arbitrary player
        handle_turn(curr_player)

        #check if game is over
        check_if_game_over()

        #flip to other player
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")


# handle single turn of an arbitrary player
def handle_turn(player):
    
    print(player + "'s turn.")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input. Choose position from 1-9: ")

        #the above variable holds string value, we need to convert it in integer -1 cause 
        #our indexing is from 0-8, so if a player choose 9 it means the index 8
        position = int(position)-1

        if board[position] == "-":
            valid = True
        else:
            print("you can't go there. go again")

    board[position] = player

    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    global winner

    #check rows
    row_winner = check_row()
    #check columns
    column_winner = check_column()
    #check diagonals
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return winner


    return

def check_row():

    global game_is_on

    #check if any of the rows have same values and not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any rows has a match flag that there is a win 
    if row_1 or row_2 or row_3:
        game_is_on = False

    #return the winner X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    
    return

def check_column():

    global game_is_on

    #check if any of the columns have same values and not empty
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    #if any columns has a match flag that there is a win 
    if col_1 or col_2 or col_3:
        game_is_on = False

    #return the winner X or O
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    
    return

def check_diagonal():

    global game_is_on

    #check if any of the diagonal have same values and not empty
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    #if any diagonal has a match flag that there is a win 
    if diag_1 or diag_2:
        game_is_on = False

    #return the winner X or O
    if diag_1:
        return board[0]
    if diag_2:
        return board[2]
    
    return

def check_if_tie():
    global game_is_on

    if "-" not in board:
        game_is_on = False
    return

def flip_player():
    global curr_player

    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"
    return



play_game()


