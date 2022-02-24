import sys
from collections import deque
sys.setrecursionlimit(10 ** 4)
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
N, M = MIS()
ground = [[*map(int, list(In()))] for i in range(N)]
visited = [[0] * M for i in range(N)]


def BFS(x, y):
  queue = deque([(x, y)])
  while queue:
    x, y = queue.popleft()
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
      if 0 <= nx < N and 0 <= ny < M:
        if ground[nx][ny] == 1:
          if not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))


visited[0][0] = 1
BFS(0, 0)
ans = visited[N - 1][M - 1]
print(ans) if ans else print(-1)
