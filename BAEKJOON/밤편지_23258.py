import sys
from heapq import heappop, heappush
def floyd():
  #init
  for i in range(1,V+1):
    for j in range(1,V+1):
      if i==j:dist[0][i][j]=0;continue
      elif ROUTE[i][j]==0:dist[0][i][j]=INF
      else: dist[0][i][j] = ROUTE[i][j]
  #find n:n shortest route
  for k in range(1,V+1):
    for i in range(1,V+1):
      for j in range(1,V+1):
        # k-th 미만의 노드를 거치면서 i to j의 최단거리는 dist[k]에 저장된다.
        # k-th 미만의 노드를 거치면서 i to j의 최단거리는 (k-1)-th미만의 노드를 거치면서 i to j를 가는 최단거리 정보와 연관.
        # k번째 미만의 노드를 모두 거치는것이 가능한 상황에서 i to j의 최단거리
        # 모두 거치는 것이 가능하다는 면에서 dp를 적용할 수 있음 : k 미만의 노드 모두 거치는 최단 거리 <-> k-1 미만의 노드 모두 거치는 최단 거리
        dist[k][i][j] = min(dist[k-1][i][j], dist[k-1][i][k]+dist[k-1][k][j])
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
print = sys.stdout.write
V, Q = MIS()
INF=float("inf")
dist = [[[INF for j in range(V+1)] for i in range(V+1)] for k in range(V+1)]
ROUTE = [[]]
for i in range(V):
  ROUTE.append([0]+[*MIS()])
floyd()
for q in range(Q):
  c, s, e = MIS()
  print("%s" % dist[c-1][s][e] + "\n") if dist[c-1][s][e] != INF else print("%s" % -1 + "\n")