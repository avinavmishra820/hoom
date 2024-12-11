import os

turn = 'X'
win = False
spaces = 9

# Function to display the board
def draw(board):
    for i in range(6, -1, -3):
        print(' ' + board[i] + '|' + board[i+1] + '|' + board[i+2])

# Function to take input from the player
def takeinput(board, spaces, turn):
    pos = -1
    print(turn + "'s turn:")
    while pos == -1:
        try:
            pos = int(input("Pick position 1-9: "))
            # Check if position is valid and empty
            if pos < 1 or pos > 9 or board[pos - 1] != ' ':
                print("Invalid position, try again.")
                pos = -1
        except ValueError:
            print("Enter a valid position")
    # Update board and decrease spaces
    spaces -= 1
    board[pos - 1] = turn
    # Switch turn
    turn = 'O' if turn == 'X' else 'X'
    return board, spaces, turn

# Function to check if there is a winner
def checkwin(board):
    # Check rows
    for i in range(0, 3):
        r = i * 3
        if board[r] != ' ' and board[r] == board[r+1] == board[r+2]:
            return board[r]
    # Check columns
    for i in range(3):
        if board[i] != ' ' and board[i] == board[i+3] == board[i+6]:
            return board[i]
    # Check diagonals
    if board[0] != ' ' and board[0] == board[4] == board[8]:
        return board[0]
    if board[2] != ' ' and board[2] == board[4] == board[6]:
        return board[2]
    return 0

# Initialize board
board = [' '] * 9

# Game loop
while not win and spaces:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen
    draw(board)
    board, spaces, turn = takeinput(board, spaces, turn)
    win = checkwin(board)

# Final display and result
draw(board)
if win:
    print(f'{win} wins')
elif not spaces:
    print("It's a draw!")
