import sys
from collections import deque, defaultdict


def coloring(N):  # 서로 떨어져있는 섬을 구분지어줌 ex) 섬(-1)... 섬(-2)... 섬(-3)... 섬(-n)
  visited = [[0] * N for i in range(N)]
  color = -1
  for i in range(N):
    for j in range(N):
      if country[i][j] == 1:
        if not visited[i][j]:
          new_country[i][j] = color
          visited[i][j] = 1
          queue = deque([(i, j)])
          while queue:
            x, y = queue.popleft()
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
              if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                  if country[x][y] == 1:
                    visited[nx][ny] = 1
                    new_country[x][y] = color
                    queue.append((nx, ny))
          color -= 1


def findBridge():  # 최소 길이의 다리를 찾아주는 함수
  global mnn
  mnn = 999
  visitedi = [0 for i in range(10000)]
  for i in range(N):
    for j in range(N):
      if new_country[i][j] < 0:  # 섬일때
        color = new_country[i][j]  # 섬 색깔
        if not visitedi[color]:
          queue = deque([(i, j)])
          visitedx = [[0] * N for i in range(N)]
          flg = False
          while queue and not flg:
            x, y = queue.popleft()
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
              if not flg:
                if 0 <= nx < N and 0 <= ny < N:
                  if not visitedx[nx][ny]:
                    if new_country[nx][ny] == 0:
                      visitedx[nx][ny] = visitedx[x][y] + 1
                      queue.append((nx, ny))
                      # queue에 append된 상황에서 그 좌표의 4방향을 탐색
                      for nnx, nny in ((nx - 1, ny), (nx + 1, ny), (nx, ny - 1), (nx, ny + 1)):
                        if 0 <= nnx < N and 0 <= nny < N:  # 좌표의 범위안
                          # 주변의 좌표가 0이 아님 and 같은 섬이 아닐때... 즉 다른 섬이 근처에 있을때
                          if new_country[nnx][nny] != 0 and new_country[nnx][nny] != color:
                            if mnn > visitedx[nx][ny]:  # 최솟값 갱신
                              mnn = visitedx[nx][ny]
                              flg = True
                              visitedi[-color] = 1
                              break


if __name__ == "__main__":
  input = sys.stdin.readline
  N = int(input().rstrip())
  country = [list(map(int, list(input().split()))) for i in range(N)]
  new_country = [[0] * N for i in range(N)]
  coloring(N)
  findBridge()
  print(mnn)
