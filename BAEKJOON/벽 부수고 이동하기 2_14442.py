import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
def BFS():
  dq = deque([(0,0,K)])
  while dq:
    x,y,z=dq.popleft()
    if x==N-1 and y==M-1:
      print(visited[x][y][z])
      return
    for nx, ny in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
      if 0<=nx<N and 0<=ny<M:
        if board[nx][ny]==1:
          if not visited[nx][ny][z-1] and 1<=z: # z가 아니라 z-1을 확인
            visited[nx][ny][z-1]=visited[x][y][z]+1
            dq.append((nx,ny,z-1))
        if board[nx][ny]==0:
          if not visited[nx][ny][z] and 0<=z:
            visited[nx][ny][z]=visited[x][y][z]+1
            dq.append((nx,ny,z))
  print(-1)


if __name__=="__main__":
  N,M,K=MIS()
  board=[[*map(int,list(In()))] for i in range(N)]
  visited=[[[0]*(K+1) for i in range(M)] for j in range(N)]
  visited[0][0] = [0]*(K+1)
  visited[0][0][K]=1
  BFS()