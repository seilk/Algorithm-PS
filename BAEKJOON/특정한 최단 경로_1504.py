import sys
from heapq import heappop, heappush


def ijk(dist, queue):
  while queue:
    w, v = heappop(queue)
    if w > dist[v]:
      continue
    for wt, to in graph[v]:
      if dist[to] > dist[v] + wt:
        dist[to] = dist[v] + wt
        heappush(queue, (wt, to))


input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(E):
  st, ed, w = map(int, input().split())
  graph[st].append((w, ed))
  graph[ed].append((w, st))
v1, v2 = map(int, input().split())
INF = 800 * 1000 * 200000 #처음에 너무 작아서 오류 생겼었음 VWE, sys.maxsize
dist_0 = [INF for i in range(N + 1)]
dist_1 = [INF for i in range(N + 1)]
dist_2 = [INF for i in range(N + 1)]
dist_0[1], dist_1[v1], dist_2[v2] = 0, 0, 0
vset = [1, v1, v2]
distset = [dist_0, dist_1, dist_2]
for v_, d_ in zip(vset, distset):
  queue = []
  heappush(queue, ((0, v_)))
  for to in graph[v_]:
    heappush(queue, (INF, to[1]))
  ijk(d_, queue)
ans = min(dist_0[v1] + dist_1[v2] + dist_2[N], dist_0[v2] + dist_2[v1] + dist_1[N]) #최소 + 최소 = 최소
print(-1) if ans >= INF else print(ans)

# 2 0
# 1 2