def print_welcome_message():
    print("Welcome to Tic Tac Toe!")
    print("You will be prompted to enter the size of the board.")
    print("Players will take turns to enter their moves.")
    print("The first player to align their marks in a row, column, "
          "or diagonal wins!")
    print("Let's get started!\n")


def print_board(board):
    n = len(board)
    for row in board:
        print(" | ".join(row))
        print("-" * (n * 2 - 1))


def check_winner(board, player):
    n = len(board)
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(n):
        if all([board[row][col] == player for row in range(n)]):
            return True
    if all([board[i][i] == player for i in range(n)]) or all(
        [board[i][n - 1 - i] == player for i in range(n)]
    ):
        return True
    return False


def get_board_size():
    while True:
        try:
            n = int(input("Enter the size of the board (n for n x n): "))
            if n <= 0:
                raise ValueError("The size must be a positive integer.")
            return n
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def get_move(player, board_size):
    while True:
        try:
            row = int(input(
                f"Player {player}, enter the row (0 to {board_size - 1}): "
            ))
            col = int(input(
                f"Player {player}, enter the column (0 to {board_size - 1}): "
            ))
            if row < 0 or row >= board_size or col < 0 or col >= board_size:
                raise ValueError(
                    f"Row and column must be between 0 and {board_size - 1}."
                )
            return row, col
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False


def announce_winner(player):
    print(f"Player {player} wins!")


def announce_tie():
    print("It's a tie!")


def play_game():
    print_welcome_message()
    n = get_board_size()
    board = [[" " for _ in range(n)] for _ in range(n)]
    players = ["X", "O"]
    current_player = 0

    for turn in range(n * n):
        print_board(board)
        row, col = get_move(players[current_player], n)
        if make_move(board, row, col, players[current_player]):
            if check_winner(board, players[current_player]):
                print_board(board)
                announce_winner(players[current_player])
                return
            current_player = 1 - current_player
        else:
            print("This spot is already taken. Try again.")

    print_board(board)
    announce_tie()


def tic_tac_toe():
    while True:
        play_game()
        play_again = input(
            "Do you want to play again? (y/n): "
        ).strip().lower()
        if play_again != 'y':
            print("Thanks for playing Tic Tac Toe!")
            break


if __name__ == "__main__":
    tic_tac_toe()
