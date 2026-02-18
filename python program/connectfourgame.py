ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + " ".join(str(i) for i in range(COLS)))

def drop_piece(board, col, piece):
    for row in reversed(board):
        if row[col] == " ":
            row[col] = piece
            return True
    return False

def check_winner(board, piece):
    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True
    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == piece for i in range(4)):
                return True
    # Diagonal /
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True
    # Diagonal \
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)
    while not game_over:
        piece = "X" if turn % 2 == 0 else "O"
        try:
            col = int(input(f"Player {piece}, choose a column (0-{COLS-1}): "))
            if 0 <= col < COLS and drop_piece(board, col, piece):
                print_board(board)
                if check_winner(board, piece):
                    print(f"Player {piece} wins!")
                    game_over = True
                elif is_full(board):
                    print("It's a tie!")
                    game_over = True
                else:
                    turn += 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Enter a valid integer.")

if __name__ == "__main__":
    play_game()
