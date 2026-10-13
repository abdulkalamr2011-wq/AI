import itertools


def tsp(graph, start):
  nodes = list(graph.keys())
  nodes.remove(start)

  min_path = None
  min_cost = float("inf")

  for perm in itertools.permutations(nodes):
    current_cost = 0
    current_path = [start] + list(perm) + [start]
    valid = True

    for i in range(len(current_path) - 1):
      u, v = current_path[i], current_path[i + 1]
      if v in graph[u]:
        current_cost += graph[u][v]
      else:
        valid = False
        break

    if valid and current_cost < min_cost:
      min_cost = current_cost
      min_path = current_path

  return min_path, min_cost


# Graph representation using adjacency dict with weights
graph = {
    "A": {"B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30},
}

path, cost = tsp(graph, "A")
print(f"Optimal TSP Path: {path} with Cost: {cost}")
