# Tic Tac Toe Game in Python

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(player, board):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def check_draw(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Function to get the player's move
def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            row, col = (move - 1) // 3, (move - 1) % 3
            if 1 <= move <= 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to play the Tic Tac Toe game
def play_game():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    # Game loop
    while True:
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        
        # Check for win or draw
        if check_win(current_player, board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
