import sys
from collections import defaultdict
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def DFS(r,c,cl):
  global p
  for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
    if 0<=nr<M and 0<=nc<N and not visited[nr][nc] and field[nr][nc]==cl:
      visited[nr][nc]=1
      p+=1
      DFS(nr,nc,cl)

if __name__ == "__main__":
  N,M=MIS()
  field = [list(In()) for i in range(M)]
  visited=[[0]*N for i in range(M)]
  SUM={"W":0,"B":0} #defaultdict 사용하면 0일 경우 출력이 되지 않음
  for i in range(M):
    for j in range(N):
      if not visited[i][j]:
        visited[i][j]=1
        p=1
        DFS(i,j,field[i][j])
        SUM[field[i][j]]+=p**2
  print(*SUM.values())