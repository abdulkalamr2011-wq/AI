def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, N):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1, N):
                return True
            board[row] = -1

    return False

def print_queens_board(board):
    N = len(board)
    for row in range(N):
        line = ["Q" if board[row] == col else "." for col in range(N)]
        print(" ".join(line))

N = 8
board = [-1] * N
if solve_n_queens(board, 0, N):
    print("8-Queens Solution:")
    print_queens_board(board)
else:
    print("No solution found.")
