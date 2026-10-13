from collections import deque


def is_valid(m, c):
  if m < 0 or c < 0 or m > 3 or c > 3:
    return False
  if m > 0 and m < c:
    return False
  if m < 3 and (3 - m) < (3 - c):
    return False
  return True


def solve_mc():
  queue = deque([(3, 3, 1, [])])
  visited = set()

  moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

  while queue:
    m, c, boat, path = queue.popleft()

    if m == 0 and c == 0:
      return path + [(m, c, boat)]

    if (m, c, boat) in visited:
      continue
    visited.add((m, c, boat))

    for dm, dc in moves:
      if boat == 1:
        nm, nc, n_boat = m - dm, c - dc, 0
      else:
        nm, nc, n_boat = m + dm, c + dc, 1

      if is_valid(nm, nc):
        queue.append((nm, nc, n_boat, path + [(m, c, boat)]))
  return None


print("Missionaries & Cannibals Steps:", len(solve_mc()) or "No solution")
