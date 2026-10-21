def display(board):
    print()
    for i in range(3):
        print(" " + " | ".join(board[i * 3:i * 3 + 3]))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

board = [" "] * 9
player = "X"

while True:
    display(board)
    move = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = player

    if check_winner(board, player):
        display(board)
        print(f"Player {player} wins!")
        break

    if " " not in board:
        display(board)
        print("It's a draw!")
        break

    player = "O" if player == "X" else "X"
