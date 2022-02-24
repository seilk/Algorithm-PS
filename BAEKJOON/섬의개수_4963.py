import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def DFS(r, c):
  global rs, cs
  for nr, nc in [(r - 1, c),
                 (r - 1, c - 1),
                 (r - 1, c + 1),
                 (r + 1, c),
                 (r + 1, c - 1),
                 (r + 1, c + 1),
                 (r, c - 1),
                 (r, c + 1)]:
    if 0 <= nr < rs and 0 <= nc < cs:
      if not visited[nr][nc]:
        if wrld[nr][nc] == 1:
          visited[nr][nc] = 1
          DFS(nr, nc)


while 1:
  cs, rs = map(int, input().split())
  if (rs, cs) == (0, 0):
    break
  wrld = [list(map(int, input().split())) for row in range(rs)]
  ans = 0
  visited = [[0] * cs for i in range(rs)]
  for r in range(rs):
    for c in range(cs):
      if not visited[r][c]:
        if wrld[r][c] == 1:
          visited[r][c] = 1
          DFS(r, c)
          ans += 1
  print(ans)
