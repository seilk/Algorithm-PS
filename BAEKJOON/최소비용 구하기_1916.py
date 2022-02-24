import sys
from heapq import heappush as hps
from heapq import heappop as hpp

input = sys.stdin.readline


def ijk():
  while queue:
    w, t = hpp(queue)  # start를 to로 뽑는다
    if dist[t] < w:
      continue
    for info in grp[t]:
      wt, to = info
      if wt + dist[t] < dist[to]:
        dist[to] = wt + dist[t]
        hps(queue, (dist[to], to))


v = int(input().rstrip())
e = int(input().rstrip())
INF = float("INF")

grp = [[] for i in range(v + 1)]
for edge in range(e):
  f, t, w = map(int, input().split())
  grp[f].append((w, t))

start, end = map(int, input().split())

dist = [INF for i in range(v + 1)]
dist[start] = 0

queue = []
for i in range(0, v + 1):
  if i == start:
    hps(queue, (0, i))
  else:
    hps(queue, (INF, i))

visited = [0] * (v + 1)
visited[start] = 1

ijk()

print(dist[end])
