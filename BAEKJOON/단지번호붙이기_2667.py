import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
town = [list(map(int, list(input().rstrip()))) for i in range(N)]


def BFS(crd, idx, cnt):
  queue = deque([crd])
  while queue:
    x, y = queue.popleft()
    for nx, ny in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
      if 0 <= nx < N and 0 <= ny < N:
        if not visited[nx][ny]:
          if town[nx][ny] == 1:
            visited[nx][ny] = idx
            queue.append((nx, ny))
            cnt += 1
  return cnt


visited = [[0 for i in range(N)] for i in range(N)]
idx = 1
ans = []
for i in range(N):
  for j in range(N):
    t = town[i][j]
    if not visited[i][j]:
      if t:
        visited[i][j] = idx
        cnt = BFS((i, j), idx, 1)
        ans.append(cnt)
        idx += 1

print(idx-1)
print(*sorted(ans), sep="\n")