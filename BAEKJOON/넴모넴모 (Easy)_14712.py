import sys


def canBreak(i, j):
  return visited[i - 1][j - 1] == 1 and visited[i - 1][j] == 1 and visited[i][j - 1] == 1


def CHECK(i, j):
  global cnt
  if i == N and j == M + 1:
    cnt += 1
    return
  cnt += 1
  for r in range(i, N + 1):
    jj = j if r == i else 1  # 중복 제거
    for c in range(jj, M + 1):
      if not canBreak(r, c):
        visited[r][c] = 1
        CHECK(r, c + 1)
        visited[r][c] = 0


if __name__ == "__main__":
  R = lambda: sys.stdin.readline().rstrip()
  MIS = lambda: map(int, R().split())
  N, M = MIS()
  MAP = [[0] * (M + 2)] + [[0] * (M + 2) for i in range(N + 1)]
  visited = [[0] * (M + 2)] + [[0] * (M + 2) for i in range(N + 1)]
  num = 1
  cnt = 0
  CHECK(1, 1)
  print(cnt)
