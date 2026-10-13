Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import heapq
... 
... 
... class Node:
... 
...   def __init__(self, state, parent, move, depth, cost):
...     self.state = state
...     self.parent = parent
...     self.move = move
...     self.depth = depth
...     self.cost = cost
... 
...   def __lt__(self, other):
...     return self.cost < other.cost
... 
... 
... def manhattan(state, goal):
...   dist = 0
...   for i in range(1, 9):
...     p1 = state.index(i)
...     p2 = goal.index(i)
...     dist += abs(p1 // 3 - p2 // 3) + abs(p1 % 3 - p2 % 3)
...   return dist
... 
... 
... def get_neighbors(state):
...   neighbors = []
...   empty = state.index(0)
...   x, y = empty // 3, empty % 3
...   moves = [("UP", -1, 0), ("DOWN", 1, 0), ("LEFT", 0, -1), ("RIGHT", 0, 1)]
...   for move, dx, dy in moves:
...     nx, ny = x + dx, y + dy
...     if 0 <= nx < 3 and 0 <= ny < 3:
...       n_empty = nx * 3 + ny
...       new_state = list(state)
...       new_state[empty], new_state[n_empty] = new_state[n_empty], new_state[empty]
      neighbors.append((tuple(new_state), move))
  return neighbors


def solve_8_puzzle(start, goal):
  pq = []
  start_node = Node(start, None, None, 0, manhattan(start, goal))
  heapq.heappush(pq, start_node)
  visited = set()

  while pq:
    current = heapq.heappop(pq)
    if current.state == goal:
      path = []
      while current.parent:
        path.append((current.move, current.state))
        current = current.parent
      return path[::-1]

    visited.add(current.state)
    for neighbor, move in get_neighbors(current.state):
      if neighbor not in visited:
        cost = current.depth + 1 + manhattan(neighbor, goal)
        heapq.heappush(
            pq, Node(neighbor, current, move, current.depth + 1, cost)
        )
  return None


# Example usage:
initial_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
solution = solve_8_puzzle(initial_state, goal_state)
