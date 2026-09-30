Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority Queue store format: (f_score, g_score, current_node, path)
    open_set = []
    heapq.heappush(open_set, (0 + heuristics[start], 0, start, [start]))
    visited = {}

    while open_set:
...         f_score, g_score, current, path = heapq.heappop(open_set)
... 
...         if current == goal:
...             return path, g_score
... 
...         if current in visited and visited[current] <= g_score:
...             continue
...         visited[current] = g_score
... 
...         for neighbor, weight in graph.get(current, {}).items():
...             tentative_g = g_score + weight
...             f_neighbor = tentative_g + heuristics.get(neighbor, 0)
...             heapq.heappush(open_set, (f_neighbor, tentative_g, neighbor, path + [neighbor]))
... 
...     return None, float('inf')
... 
... # Weighted Graph
... graph = {
...     'A': {'B': 1, 'C': 3},
...     'B': {'D': 1, 'E': 4},
...     'C': {'E': 1},
...     'D': {'G': 6},
...     'E': {'G': 2},
...     'G': {}
... }
... 
... # Heuristic values h(n) to Goal 'G'
... heuristics = {
...     'A': 6,
...     'B': 4,
...     'C': 3,
...     'D': 5,
...     'E': 1,
...     'G': 0
... }
... 
... path, cost = a_star_search(graph, heuristics, 'A', 'G')
... print(f"A* Path: {' -> '.join(path)}")
