import sys
from collections import deque


def BFS(i, j):
  dq = deque([(i, j)])
  info = deque([])
  while dq:
    r, c = dq.popleft()
    seanum = 0  # pop한 좌표에 관한 주변 바다의 개수
    visited[r][c] = 1
    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
      if 0 <= nr < N and 0 <= nc < M:
        if not visited[nr][nc]:
          if MAP[nr][nc] > 0:
            dq.append((nr, nc))
            visited[nr][nc] = 1
          else:  # 만약 주변 땅이 0이면 바다를 저장함
            seanum += 1
    if seanum > 0:  # 바다의 개수와 주변 땅을 한꺼번에 구함
      info.append([r, c, seanum])
  return info


def solve():
  global visited
  year = 0
  A = True
  while A:
    allzero = True
    cnt = 0
    visited = [[0] * M for i in range(N)]
    for i in range(1, N - 1):
      for j in range(1, M - 1):
        if MAP[i][j] != 0:
          if not visited[i][j]:
            allzero = False
            cnt += 1
            if cnt < 2:
              info = BFS(i, j)
              while info:
                r, c, m = info.popleft()
                MAP[r][c] = max(0, MAP[r][c] - m)
            else:
              A = False
              break
      if A == False:
        break
    if A == False:
      print("%s" % year + "\n")
      break
    if allzero:
      print("%s" % 0 + "\n")
      break
    year += 1


if __name__ == "__main__":
  input = sys.stdin.readline
  print = sys.stdout.write
  N, M = map(int, input().split())
  MAP = [[*map(int, input().split())] for i in range(N)]
  solve()
