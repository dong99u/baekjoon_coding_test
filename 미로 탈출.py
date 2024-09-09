from collections import deque
import sys

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, sys.stdin.readline().rstrip().split())


maze = [
    list(map(int, sys.stdin.readline().rstrip()))
    for _ in range(n)
]
queue = deque()

queue.append((0, 0))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue

        if maze[nx][ny] == 0:
            continue

        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))


print(maze[n - 1][m - 1])