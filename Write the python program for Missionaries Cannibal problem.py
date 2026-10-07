from collections import deque

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and \
           (m == 0 or m >= c) and \
           (3-m == 0 or 3-m >= 3-c)

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    q = deque([(start, [start])])
    visited = {start}

    while q:
        (m, c, boat), path = q.popleft()

        if (m, c, boat) == goal:
            for state in path:
                print(state)
            return

        for dm, dc in moves:
            if boat == 0:
                new = (m-dm, c-dc, 1)
            else:
                new = (m+dm, c+dc, 0)

            if valid(new[0], new[1]) and new not in visited:
                visited.add(new)
                q.append((new, path + [new]))

solve()
