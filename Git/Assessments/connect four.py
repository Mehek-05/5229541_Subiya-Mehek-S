# hi 


import numpy as np

def create_board():
    # Create a 6x7 matrix filled with zeros
    return np.zeros((6, 7), dtype=int)

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def drop_piece(board, row, col, player):
    board[row][col] = player

def is_valid_move(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            return row

def check_win(board, player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # Check vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # Check diagonals
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True
            if board[row][col + 3] == player and board[row + 1][col + 2] == player and board[row + 2][col + 1] == player and board[row + 3][col] == player:
                return True

    return False

def main():
    board = create_board()
    player = 1

    while True:
        print_board(board)
        col = int(input(f"Player {player}, choose a column (0-6): "))
        
        if is_valid_move(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, player)

            if check_win(board, player):
                print(f"Player {player} wins!")
                break

            player = 3 - player  # Switch players (1 -> 2, 2 -> 1)
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
