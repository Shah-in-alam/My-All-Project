import random

# board bananor jonno code 
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# kmne kmne jita jai oi ta jannar jonno code
def check_winner(board, player):
    # logic kmne hocca daka jak 
    for i in range(3):
        if all([spot == player for spot in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([spot != ' ' for row in board for spot in row])

# Function for the human player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("This spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Function for the AI opponent's move
def ai_move(board):
    # AI chooses a random available spot
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    move = random.choice(available_moves)
    board[move[0]][move[1]] = 'O'

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's move
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations, you win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI opponent's move
        ai_move(board)
        print("AI has made its move:")
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()
