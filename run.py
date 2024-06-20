def print_welcome_message():
    """
    Prints a welcome message to the players.
    """
    print("Welcome to Tic Tac Toe!")
    print("You will be prompted to enter the size of the board.")
    print("Players will take turns to enter their moves.")
    print("The first player to align their marks in a row, column, or diagonal wins!")
    print("Let's get started!\n")

def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.
    """
    n = len(board)
    for row in board:
        print(" | ".join(row))
        print("-" * (n * 2 - 1))
