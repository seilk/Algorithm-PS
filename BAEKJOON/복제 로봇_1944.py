from collections import deque
from heapq import heappush, heappop
import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def bfs(x,y):
  global ans, hq
  INF = float("inf")
  vist = [[-1]*N for i in range(N)]
  vist[x][y]=0
  dq = deque([(x,y)])
  while dq:
    x,y = dq.popleft()
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
      if 0<=nx<N and 0<=ny<N and miro[nx][ny]!=1:
        if vist[nx][ny]<0:
          vist[nx][ny]=vist[x][y]+1
          if miro[nx][ny]=="K":
            heappush(hq, (vist[nx][ny], nx, ny))
          dq.append((nx,ny))

def findS(miro):
  pointS = (0,0)
  INF = float("inf")
  for i in range(N):
    for j in range(N):
      if miro[i][j] == "S":
        pointS=(i, j)
        check[i][j] = 0
      elif miro[i][j] == "K":
        check[i][j] = INF
      elif miro[i][j] != "S" and miro[i][j] != "K":
        miro[i][j] = int(miro[i][j])
  return pointS

N, M = MIS()
miro = [list(In()) for i in range(N)]
check = [[0]*N for i in range(N)]
vistn = [[0]*N for i in range(N)]
x,y=findS(miro)
hq=[(0, x, y)]
INF = float("inf")
while hq:
  w, x, y=heappop(hq)
  if vistn[x][y] == 0:
    vistn[x][y] = 1
    check[x][y] = w
    bfs(x,y)
ans= sum(sum(check[i]) for i in range(N))
print(-1) if ans == INF else print(ans)

# 5 5
# 11111
# 1S0K1
# 1K1K1
# 1K1K1
# 11111

# 7 4
# 1111111
# 1S000K1
# 1000001
# 100K001
# 100K001
# 1K000K1
# 1111111