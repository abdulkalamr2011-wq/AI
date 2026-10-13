from collections import deque


def water_jug(jug1_capacity, jug2_capacity, target):
  visited = set()
  queue = deque([(0, 0, [])])

  while queue:
    j1, j2, path = queue.popleft()

    if j1 == target or j2 == target:
      return path + [(j1, j2)]

    if (j1, j2) in visited:
      continue
    visited.add((j1, j2))

    states = [
        (jug1_capacity, j2, "Fill Jug 1"),
        (j1, jug2_capacity, "Fill Jug 2"),
        (0, j2, "Empty Jug 1"),
        (j1, 0, "Empty Jug 2"),
        (
            j1 - min(j1, jug2_capacity - j2),
            j2 + min(j1, jug2_capacity - j2),
            "Pour Jug 1 to Jug 2",
        ),
        (
            j1 + min(j2, jug1_capacity - j1),
            j2 - min(j2, jug1_capacity - j1),
            "Pour Jug 2 to Jug 1",
        ),
    ]

    for next_j1, next_j2, action in states:
      if (next_j1, next_j2) not in visited:
        queue.append((next_j1, next_j2, path + [(j1, j2, action)]))
  return None


print("Water Jug Path:", water_jug(4, 3, 2))
