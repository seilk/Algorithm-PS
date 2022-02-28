import sys
from heapq import *
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
INF = float("inf")
def dijk(start):
  dist = [INF]*(1+V)
  pq = [(0, start)]

  while pq:
    dd, cur = heappop(pq)
    if dist[cur]!=INF: continue
    dist[cur]=dd
    for d, b in grp[cur]:
      if dist[b] > dist[cur] + d:
        heappush(pq, (dist[cur] + d, b))

  return dist

V, E = MIS()
grp = [[] for i in range(1+V)]
for e in range(E):
  a, b, d = MIS()
  grp[a].append((d,b))
  grp[b].append((d,a))
m1, m2 = MIS()

startFrom1 = dijk(1)
startFromM1 = dijk(m1)
startFromM2 = dijk(m2)
ans = min(startFrom1[m1]+startFromM1[m2]+startFromM2[V],
          startFrom1[m2]+startFromM2[m1]+startFromM1[V])
print(-1) if ans == INF else print(ans)


