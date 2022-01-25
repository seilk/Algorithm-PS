import sys


def canBreak(i, j): # 왼->오 , 위->아래 방향으로 탐색할거라서 위쪽으로 만들어질 수 있는 사각형만 파악하면 됨.
  return visited[i - 1][j - 1] == 1 and visited[i - 1][j] == 1 and visited[i][j - 1] == 1


def CHECK(i, j):
  global cnt
  if i == N and j == M + 1:
    cnt += 1
    return
  cnt += 1
  for r in range(i, N + 1): # 2차원 백트래킹 중복 제거 인덱스 값 조정 : i부터~
    jj = j if r == i else 1  # 같은 행일때는 j부터 해야하고 더 아래쪽 행일때는 1부터 탐색
    for c in range(jj, M + 1): # 1또는 j부터~
      if not canBreak(r, c):
        visited[r][c] = 1
        CHECK(r, c + 1)
        visited[r][c] = 0


if __name__ == "__main__":
  R = lambda: sys.stdin.readline().rstrip()
  MIS = lambda: map(int, R().split())
  N, M = MIS()
  MAP = [[0] * (M + 2)] + [[0] * (M + 2) for i in range(N + 1)]
  visited = [[0] * (M + 2)] + [[0] * (M + 2) for i in range(N + 1)] #체킹에 편하게끔 위,아래,왼,오에 한줄씩 더 생성함
  num = 1
  cnt = 0
  CHECK(1, 1)
  print(cnt)
