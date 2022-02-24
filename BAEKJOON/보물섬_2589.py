import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def BFS(i,j,k):
  global mxx
  dq=deque([(i,j)])
  visited[i][j]=0
  while dq:
    r,c = dq.popleft()
    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
      if 0<=nr<R and 0<=nc<C and visited[nr][nc]==-1 and maap[nr][nc]==k:
        visited[nr][nc]=visited[r][c]+1
        dq.append((nr,nc))
  mxx=max(mxx, visited[r][c])


if __name__=="__main__":
  R,C=MIS()
  mxx=0
  maap=[list(In()) for i in range(R)]
  for r in range(R):
    for c in range(C):
      if maap[r][c]=="L":
        visited=[[-1]*C for i in range(R)]
        BFS(r,c,maap[r][c])
  print(mxx)

# 3 5
# LLLWL
# LWLWL
# LWLLL
#
# 3 3
# LLL
# LWL
# LWL