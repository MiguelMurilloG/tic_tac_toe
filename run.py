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

def check_winner(board, player):
    """
    Checks if the current player has won the game.
    """
    n = len(board)
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(n):
        if all([board[row][col] == player for row in range(n)]):
            return True
    if all([board[i][i] == player for i in range(n)]) or all([board[i][n - 1 - i] == player for i in range(n)]):
        return True
    return False

def get_board_size():
    """
    Prompts the user to enter the board size and validates the input.
    """
    while True:
        try:
            n = int(input("Enter the size of the board (n for n x n): "))
            if n <= 0:
                raise ValueError("The size must be a positive integer.")
            return n
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def get_move(player, board_size):
    """
    Prompts the player to enter their move and validates the input.
    """
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0 to {board_size-1}): "))
            col = int(input(f"Player {player}, enter the column (0 to {board_size-1}): "))
            if row < 0 or row >= board_size or col < 0 or col >= board_size:
                raise ValueError(f"Row and column must be between 0 and {board_size-1}.")
            return row, col
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def make_move(board, row, col, player):
    """
    Places the player's move on the board if the spot is empty.
    """
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def announce_winner(player):
    """
    Announces the winner of the game.
    """
    print(f"Player {player} wins!")

def announce_tie():
    """
    Announces a tie.
    """
    print("It's a tie!")
