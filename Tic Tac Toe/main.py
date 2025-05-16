# EVERYTHING OTHER THAN THE make_computer_move() AND PART OF THE winner() FUNCTIONS ARE NOT MINE!!!!!

import random

def winner(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    If there is no winner, the function will return the empty string "".
    If the user has won, it will return "X", and if the computer has
    won it will return "O"."""

    # Check rows for winner
    for row in range(3): # Loop through all 3 rows
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != " "): # Check if each consecutive element in the current row is equivalent and check if it is a blank space
            return board[row][0] # Return the board with the symbol of the player that won 

    # Check columns for winner
    for col in range(3): # Loops through all the collums
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col] != " ": # checks if each element in the current column is identical while making sure the elements are not blank spaces
            return board[0][col] # Returns the symbol that is lined up in a row indicating which player won

    # Check diagonal (top-left to bottom-right) for winner

    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " "): # Checks that the diagonal from the top-left to bottom-right have identical elements while making sure that they are not just blank spaces.
        return board[0][0] # returns the symbol that is lined up in the diagonal, indicating which player won.

    # Check diagonal (bottom-left to top-right) for winner

    if (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " "): # Checks that the diagonal from the bottom-left to the top-right have indentical elements while making sure that they are not just blank spaces.
        return board[0][2] # Returns the symbol that is lined up in the diagonal, indicating which player won.

    # No winner: return the empty string
    return ""

def display_board(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will print the Tic-Tac-Toe board grid (using ASCII characters)
    and show the positions of any Xs and Os.  It also displays
    the column and row numbers on top and beside the board to help
    the user figure out the coordinates of their next move.
    This function does not return anything."""

    print ("   0   1   2") #prints the labling of each column
    print ("0: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2]) #Prints the lable of the row while printing the top vertical borders
    print ("  ---+---+---") # Prints the top horizontal border
    print ("1: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2]) # Prints the lable of the row while printing the middle vertical borders
    print ("  ---+---+---") # Prints the bottom horizontal border
    print ("2: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2]) # Prints the lable of the row while printing the bottom vertical borders
    print ()

def make_user_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will ask the user for a row and column.  If the row and
    column are each within the range of 0 and 2, and that square
    is not already occupied, then it will place an ÒXÓ in that square."""

    valid_move = False # Serves as the condition for the while loop. If the move made is a valid move the players turn ends. Since the player has not yet made a move it starts as false.
    while not valid_move: # Lets to code run over again if the players inputed coordinates are already taken up or if the inputed coordinates do not exist on the board.
        row = int(input("What row would you like to move to (0-2):")) # Asks the player for the row they want to place their move in.
        col = int(input("What col would you like to move to (0-2):")) # Asks the player for the column they want to place their move in.
        if (0 <= row <= 2) and (0 <= col <= 2) and (board[row][col] == " "): # This conditional statement makes sure the players inputed move is both a location on the board and that the chosen square is empty.
            board[row][col] = 'X' # Inputs an "X" into the players chosen coordinate
            valid_move = True # Ends the players turn
        else:
            print ("Sorry, invalid square. Please try again!\n") # Tells the player their input is invalid.


def make_computer_move(board): # Function to control the computers moves.
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will randomly pick row and column values between 0 and 2.
    If that square is not already occupied it will place an ÒOÓ
    in that square.  Otherwise, another random row and column
    will be generated."""

    row = random.randint(0,2) # The computer randomly generates a number from 0-2 in order to choose its row coordinate.
    col = random.randint(0,2) # The computer randomly generates a number from 0-2 in order to choose its colomn coordinate.

    while board[row][col] != " ": # this loop makes the computer regenerate their coordinates untill they are on an empty square if the original coordinate was not empty.

        row = random.randint(0,2) # Randomly generates the row coordinate.
        col = random.randint(0,2) # Randomly generates the colomn coordinate.

    board[row][col] = "O" # Inputs an "O" into the computers coordinate.

def main():
    """Our Main Game Loop:"""

    free_cells = 9
    users_turn = True
    ttt_board = [ [ " ", " ", " " ], [ " ", " ", " " ], [ " ", " ", " " ] ]

    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1

    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print ("Y O U   W O N !")
    elif (winner(ttt_board) == 'O'):
        print ("I   W O N !")
    else:
        print ("S T A L E M A T E !")
    print ("\n*** GAME OVER ***\n")

# Start the game!
main()