import random

def print_board(board):
    for row in board:
        print("  |   ".join(row))
        print("-" * 15)
print("             LETS PLAY THE GAME           ")


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return (move - 1) // 3, (move - 1) % 3
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    user_symbol = 'X'
    computer_symbol = 'O'

    while True:
        print_board(board)

        # User move
        user_row, user_col = user_move(board)
        board[user_row][user_col] = user_symbol

        if check_winner(board, user_symbol):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Computer move
        print("\nComputer's turn:")
        computer_row, computer_col = computer_move(board)
        board[computer_row][computer_col] = computer_symbol

        if check_winner(board, computer_symbol):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
