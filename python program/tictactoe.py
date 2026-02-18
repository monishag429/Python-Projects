import math

# Print the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for winner
def check_winner(board):
    # Rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Check if board is full (Draw)
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Get available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r, c in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

# AI move
def ai_move(board):
    best_score = -math.inf
    move = None
    for r, c in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

# Main game function
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe (You vs AI)\n")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Your move - Row (0-2): "))
                col = int(input("Your move - Column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("That cell is occupied!")
            except (ValueError, IndexError):
                print("Invalid input! Please enter 0, 1, or 2.")
        
        print_board(board)

        if check_winner(board):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        r, c = ai_move(board)
        board[r][c] = "O"
        print_board(board)

        if check_winner(board):
            print("💻 AI wins!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
