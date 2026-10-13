Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def print_board(board):
...   for row in board:
...     print(" ".join("Q" if x == 1 else "." for x in row))
...   print()
... 
... 
... def is_safe(board, row, col):
...   for i in range(col):
...     if board[row][i] == 1:
...       return False
...   for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
...     if board[i][j] == 1:
...       return False
...   for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
...     if board[i][j] == 1:
...       return False
...   return True
... 
... 
... def solve_nq_util(board, col):
...   if col >= len(board):
...     return True
...   for i in range(len(board)):
...     if is_safe(board, i, col):
...       board[i][col] = 1
...       if solve_nq_util(board, col + 1):
...         return True
...       board[i][col] = 0
...   return False
... 
... 
... def solve_8_queen():
...   board = [[0] * 8 for _ in range(8)]
...   if solve_nq_util(board, 0):
...     print_board(board)
...   else:
...     print("Solution does not exist")
... 
... 
