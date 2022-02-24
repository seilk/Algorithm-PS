import sys
from itertools import combinations
def FW(N, arr):
  dist=[[0]*(N+1) for i in range(N+1)]
  for i in range(1,N+1):
    for j in range(1,N+1):
      if i==j:
        dist[i][j] = 0
      else:
        dist[i][j] = arr[i][j]
  for k in range(1,N+1):
    for i in range(1,N+1):
      for j in range(1,N+1):
        dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])
  return dist

if __name__=="__main__":
  In = lambda : sys.stdin.readline().rstrip()
  MIS = lambda : map(int, In().split())
  V,E = MIS()
  INF = float("inf")
  arr=[[INF for i in range(V+1)] for j in range(V+1)]
  for e in range(E):
    a,b = MIS()
    arr[a][b]=2
    arr[b][a]=2
  dist = FW(V,arr)
  comb = combinations([i+1 for i in range(V)],2)
  MINN = [INF,INF,INF] # 시작노드, 끝노드,
  for x,y in comb:
    SUM = 0 # 초기화
    for v in range(1,V+1):
      if v == x or v == y:
        continue
      SUM+=min(dist[x][v], dist[y][v])
    if MINN[2]>SUM:
      MINN=[x,y,SUM]
    elif MINN==SUM:
      if min(MINN[1],MINN[2]) > min(x,y):
        MINN=[x,y,SUM]
      elif min(MINN[1],MINN[2]) == min(x,y) and max(MINN[1],MINN[2]) > max(x,y):
        MINN=[x,y,SUM]
  print(*sorted(MINN[:2]), MINN[2])
