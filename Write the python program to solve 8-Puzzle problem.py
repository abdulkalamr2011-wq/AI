from collections import deque

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row, col = divmod(idx, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            state_list = list(state)
            state_list[idx], state_list[new_idx] = state_list[new_idx], state_list[idx]
            neighbors.append(tuple(state_list))
    return neighbors

def solve_8_puzzle(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current, path = queue.popleft()
        if current == goal_state:
            return path + [current]

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current]))

    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Example run
start = (1, 2, 3, 4, 0, 5, 6, 7, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
solution = solve_8_puzzle(start, goal)

if solution:
    print(f"Solved in {len(solution) - 1} steps:")
    for step in solution:
        print_board(step)
