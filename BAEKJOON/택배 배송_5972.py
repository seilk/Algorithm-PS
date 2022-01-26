import sys
from heapq import heappop, heappush


def DAIK():
  hq = []
  heappush(hq, (0, 1))
  while hq:
    weight, node = heappop(hq)
    if dist[node] < weight:
      break
    for wweight, nnode in graph[node]:
      if dist[nnode] > dist[node] + wweight:
        dist[nnode] = dist[node] + wweight
        heappush(hq, (wweight, nnode))

if __name__ == "__main__":
  R = lambda: sys.stdin.readline().rstrip()
  MIS = lambda: map(int, R().split())
  V, E = MIS()
  graph = [[] for i in range(V + 1)]
  INF = float("inf")
  for e in range(E):
    start, end, weight = MIS()
    graph[start].append((weight, end))
    graph[end].append((weight, start))
  dist = [INF] * (V + 1)
  dist[1] = 0
  DAIK()
  print(dist[V])