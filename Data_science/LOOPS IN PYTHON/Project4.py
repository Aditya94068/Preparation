def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input. Try again.")
                continue

            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                break

            if check_draw(board):
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number (0, 1, or 2).")

# Run the game
tic_tac_toe()
