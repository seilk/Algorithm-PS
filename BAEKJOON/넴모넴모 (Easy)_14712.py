# TLE
import sys


def canBreak(i, j):
  return visited[i - 1][j - 1] == 1 and visited[i - 1][j] == 1 and visited[i][j - 1] == 1


def CHECK(i, j, prev):
  global cnt
  if i == N and j == M + 1:  # 노드의 마지막까지 도달했을때. return
    cnt += 1
    return
  for r in range(1, N + 1): #애초에 1부터 시작하는 DFS는 시간초과 날 확률이 높음!, 불필요한 인덱스는 돌지 않게끔 코드 짤 것
    for c in range(1, M + 2):
      if numbering[r][c] > prev:
        if not canBreak(r, c):  # 해당 좌표에 넴모를 두었을때 파괴가 가능한 상황 확인.
          visited[r][c] = 1
          CHECK(r, c, numbering[r][c])
          visited[r][c] = 0


if __name__ == "__main__":
  R = lambda: sys.stdin.readline().rstrip()
  MIS = lambda: map(int, R().split())
  print = sys.stdout.write
  N, M = MIS()
  MAP = [[0] * (M + 2)] + [[0] * (M + 2) for i in range(N + 1)]
  visited = [[0] * (M + 2)] + [[0] * (M + 2) for i in range(N + 1)]
  numbering = [[0] * (M + 2)] + [[0] * (M + 2) for i in
                                 range(N + 1)]  # 넘버링하는건 시간초과 발생함. DFS문 안에서 인덱스 값 조절로 중복 제거 하는것이 유리
  num = 1
  for i in range(1, N + 1):
    for j in range(1, M + 1):
      numbering[i][j] = num
      num += 1
  numbering[N][M + 1] = num
  cnt = 0
  CHECK(1, 1, 0)
  print("%s" % cnt)
