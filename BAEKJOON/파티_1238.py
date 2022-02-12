import sys
from heapq import heappush, heappop
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def daik(x):
  hq=[]; heappush(hq,(0,x));
  while hq:
    w,s = heappop(hq)
    if w > dist[s]:continue
    for nw, nd in grp[s]:
      if dist[nd] > dist[s]+nw:
        dist[nd]=dist[s]+nw
        heappush(hq,(dist[nd], nd))

  #distRv
  hq=[]; heappush(hq,(0,x));
  while hq:
    w,s = heappop(hq)
    if w > distRv[s]:continue
    for nw, nd in grpRv[s]:
      if distRv[nd] > distRv[s]+nw:
        distRv[nd]=distRv[s]+nw
        heappush(hq,(distRv[nd], nd))

V,E,X=MIS() #학생수(노드수), 간선 수, 마을 목표지점
grp=[[] for i in range(V+1)]
grpRv=[[] for i in range(V+1)]
for e in range(E):
  st,ed,wt=MIS()#시작점, 끝점, 가중치
  grpRv[ed].append((wt,st)) # 반대방향의 간선을 따로 저장해줌
  grp[st].append((wt,ed))
INF=float("inf")
dist, distRv=[INF]*(V+1),[INF]*(V+1)
dist[X], distRv[X]=0, 0 # 두 최단거리 리스트의 출발지점은 동일함
daik(X)
answer=[a+b for a,b in zip(dist[1:], distRv[1:])]
print(max(answer))
