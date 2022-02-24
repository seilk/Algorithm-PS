import sys
from collections import deque


def BFS():
  INF = 1_000_002
  dq = deque([(1, 1, 1)])  # x좌표, y좌표, chance 여부
  visited = [[[0, 0] for j in range(M + 1)] for i in range(N + 1)]  # 방문여부
  distance = [[[0, 0] for j in range(M + 1)] for i in range(N + 1)]  # 최단거리 저장
  distance[1][1][0], distance[1][1][1], distance[N][M][0], distance[N][M][1] = 1, 1, INF, INF  # 최단거리 초기화
  while dq:
    r, c, w = dq.popleft()
    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
      if 1 <= nr <= N and 1 <= nc <= M:
        if w == 1:  # 아직 벽을 부수지 않은 경우
          if MAP[nr][nc] == 1 and not visited[nr][nc][0]:
            visited[nr][nc][0] = 1
            dq.append((nr, nc, 0))  # 이번에 부순 경우
            distance[nr][nc][0] = distance[r][c][1] + 1
          if MAP[nr][nc] == 0 and not visited[nr][nc][1]:
            visited[nr][nc][1] = 1
            dq.append((nr, nc, 1))
            distance[nr][nc][1] = distance[r][c][1] + 1
        if w == 0:  # 벽을 부순 경우
          if MAP[nr][nc] == 0 and not visited[nr][nc][0]:
            visited[nr][nc][0] = 1
            dq.append((nr, nc, 0))
            distance[nr][nc][0] = distance[r][c][0] + 1
  return distance[N][M]


def solve(N, M):
  mnn = 1_000_002
  tmp = BFS() # [dist1 , dist2]
  mnn = min(mnn, min(tmp))
  if (N, M) == (1, 1):
    print(1)
  elif mnn == 1_000_002:
    print(-1)
  else:
    print(mnn)


if __name__ == "__main__":
  input = sys.stdin.readline
  N, M = map(int, input().split())
  MAP = [[2] * (M + 2)] + [[2] + list(map(int, input().rstrip())) + [2] for i in range(N)] + [[2] * (M + 2)]
  solve(N, M)
