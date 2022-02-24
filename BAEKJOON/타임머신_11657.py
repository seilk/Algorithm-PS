import sys
R = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, R().split())

def find():
  for v in range(1,V+1): #1->2->3->4->5->6 (최악의 경우)
    for e in edges:
      a,b,c = e
      if dist[a]!=INF: #한번이라도 도달한 지점만 확인
        #기존에 b까지 도착하는데 걸린 최단 거리와 새로운 값 비교
        if dist[b] > dist[a]+c:
          dist[b]=dist[a]+c

# 1->2->3->7 4->5->6->7->4
  # 음의사이클 확인
  for v in range(1,V+1):
    for e in edges:
      a,b,c = e
      if dist[a]!=INF:
        if dist[b] > dist[a]+c:
          return False
  return dist


V,E=MIS()
INF=float("inf")
grp=[[INF]*(V+1) for i in range(V+1)]
edges=[]
for i in range(E):
  a,b,c=MIS()
  edges.append((a,b,c)) #출발, 도착, 가중치
dist=[INF]*(V+1)
dist[1]=0
if find():
  for i in range(2,V+1): print(dist[i]) if dist[i]!=INF else print(-1)
else: print(-1)

