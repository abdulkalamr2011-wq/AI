def dfs(graph, node, visited=None):
  if visited is None:
    visited = set()
  visited.add(node)
  traversal = [node]

  for neighbor in graph[node]:
    if neighbor not in visited:
      traversal.extend(dfs(graph, neighbor, visited))
  return traversal


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}
print("DFS Traversal:", dfs(graph, "A"))
