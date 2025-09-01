#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    """Retourne 'X' ou 'O' si un gagnant existe, sinon None."""
    # Lignes
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return row[0]
    # Colonnes
    for c in range(len(board[0])):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # Diagonales
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Out of range. Please enter 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
