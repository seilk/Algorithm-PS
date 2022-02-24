# ----------Title
# 적록색약
# Gold V
# https://www.acmicpc.net/problem/10026

# ----------Tip
# BFS
# 구현

# ----------URLs


# ----------Code with Detail
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
fld = [list(input().rstrip()) for i in range(n)]
v0 = [[0]*n for i in range(n)]
v1 = [[0]*n for i in range(n)]
d0 = {"R": 0, "G": 0, "B": 0}
d1 = {"RG": 0, "B": 0}


def BFS(crd: tuple, clr: str) -> None:
  queue = deque([crd])
  while queue:
    r, c = queue.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
      if 0 <= nr < n and 0 <= nc < n:
        if fld[nr][nc] == clr:
          if not v0[nr][nc]:
            queue.append((nr, nc))
            v0[nr][nc] = 1
  d0[clr] += 1


def BFS2(crd: tuple, clr: str) -> None:
  queue = deque([crd])
  if clr == "RG":
    while queue:
      r, c = queue.popleft()
      for nr, nc in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
        if 0 <= nr < n and 0 <= nc < n:
          if fld[nr][nc] == "R" or fld[nr][nc] == "G":
            if not v1[nr][nc]:
              queue.append((nr, nc))
              v1[nr][nc] = 1
  else:
    while queue:
      r, c = queue.popleft()
      for nr, nc in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
        if 0 <= nr < n and 0 <= nc < n:
          if fld[nr][nc] == "B":
            if not v1[nr][nc]:
              queue.append((nr, nc))
              v1[nr][nc] = 1

  d1[clr] += 1


for i in range(n):
  for j in range(n):
    if not v0[i][j]:
      v0[i][j] = 1
      BFS((i, j), fld[i][j])

    if not v1[i][j]:
      v1[i][j] = 1
      cl = "B" if fld[i][j] == "B" else "RG"
      BFS2((i, j), cl)

print(sum(d0.values()), sum(d1.values()))
