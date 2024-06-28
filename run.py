import random


def print_welcome_message():
    print("WELCOME TO")
    print("Tic-Tac-Toe")
    print("\nUse this board as a guide when placing your X or O. Each number")
    print("corresponds to a cell on the board.")
    print("\n 1 | 2 | 3 ")
    print(" ---------")
    print(" 4 | 5 | 6 ")
    print(" ---------")
    print(" 7 | 8 | 9 \n")


def print_instructions():
    print("Instructions:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players take turns to place their mark (X or O) on the board.")
    print("3. The first player to get three marks in a row (horizontally, "
          "vertically, or diagonally) wins.")
    print("4. If all cells are filled without any player winning, "
          "the game is a tie.")
    print("5. You can choose the difficulty level for the computer opponent.")
    print("   - 'easy' for a random move by the computer.")
    print("   - 'hard' for a challenging move by the computer using the "
          "minimax algorithm.")
    print()


def print_board(board):
    print("\nHere is the active game board:\n")
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print(" ---------")


def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions


def get_move(player, board):
    while True:
        try:
            move = int(input(f"Where would you like to place your {player}? "))
            if move < 1 or move > 9:
                raise ValueError
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == " ":
                return row, col
            else:
                print("\nInvalid entry: This cell is already occupied. "
                      "Please enter another number.")
        except ValueError:
            print("\nInvalid entry: Please enter a valid number between 1 "
                  "and 9.")


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score


def computer_move(board, level):
    if level == "easy":
        available_moves = [
            (r, c) for r in range(3)
            for c in range(3) if board[r][c] == " "
        ]
        return random.choice(available_moves)
    else:
        best_score = float('-inf')
        move = None
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, 0, False)
                    board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move


def play_game(level="hard"):
    print_welcome_message()
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    for turn in range(9):
        print_board(board)
        if players[current_player] == "X":
            row, col = get_move("X", board)
        else:
            print("\nComputer is making its move...\n")
            row, col = computer_move(board, level)
            print("Computer has chosen to place their O in cell "
                  f"{row * 3 + col + 1}.\n")

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"\nPlayer {players[current_player]} wins!\n")
            return

        current_player = 1 - current_player

    print_board(board)
    print("\nIt's a tie!\n")


def main_menu():
    while True:
        print("WELCOME TO")
        print("Tic Tac Toe")
        print("\nWhat would you like to do now?")
        print("1 - Read Instructions")
        print("2 - Start a New Game")
        print("3 - Exit")
        choice = input("Enter a number: ").strip()

        if choice == "1":
            print_instructions()
        elif choice == "2":
            level = input("Choose level (easy or hard): ").strip().lower()
            play_game(level)
        elif choice == "3":
            print("Thanks for playing Tic Tac Toe!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
