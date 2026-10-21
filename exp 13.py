def minimax(depth, node, maximizing, values):
    if depth == 2:
        return values[node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, node * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node * 2 + i, True, values)
            best = min(best, val)
        return best


values = [3, 5, 2, 9]
result = minimax(0, 0, True, values)

print("Best value:", result)
