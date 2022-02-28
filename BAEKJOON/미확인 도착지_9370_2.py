import sys
from heapq import *
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
INF = float("inf")

def dijk(start):
  dist = [INF]*(1+V)
  hq = [(0,start)]
  while hq:
    w, cur = heappop(hq)
    if dist[cur]!=INF : continue
    dist[cur]=w
    for d, b in grp[cur]:
      if dist[b] > dist[cur] + d:
        heappush(hq, (dist[cur] + d, b))
  return dist

T = int(In())
for t in range(T):
  V, E, R = MIS()
  S, X, Y = MIS()

  grp = [[] for i in range(V+1)]
  for e in range(E):
    a, b, d = MIS()
    grp[a].append((d,b))
    grp[b].append((d,a))
    if {a,b}=={X,Y}:
      mustPath=d

  distFromS = dijk(S)
  distFromX = dijk(X)
  distFromY = dijk(Y)

  ans = []
  for r in range(R):
    cp = int(In())
    if distFromS[cp]!=INF and distFromS[cp] == min(distFromS[X] + mustPath + distFromY[cp],
                                                    distFromS[Y] + mustPath + distFromX[cp]):
      ans.append(cp)
  ans.sort()
  print(*ans)