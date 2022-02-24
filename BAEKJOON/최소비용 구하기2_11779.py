import sys
from heapq import heappush as hps
from heapq import heappop as hpp


def ijk():
  while queue:
    w, t = hpp(queue)
    if w > dist[t][0]:  # 출발점에서 t까지 가는 비용
      continue
    for wt, to in grp[t]:  # t -> to 경로
      if dist[to][0] > dist[t][0] + wt:
        dist[to] = (dist[t][0] + wt, dist[t][1] + [to])
        hps(queue, (dist[to][0], to))


if __name__ == "__main__":
  input = sys.stdin.readline
  v = int(input().rstrip())
  e = int(input().rstrip())

  grp = [[] for i in range(v + 1)]
  for i in range(e):
    f, t, w = map(int, input().split())
    grp[f].append((w, t))

  start, end = map(int, input().split())

  INF = 9876543210
  dist = [(INF, [i]) for i in range(v + 1)]
  dist[start] = (0, [start])

  queue = []
  for i in range(0, v + 1):
    if i == start:
      hps(queue, (0, start))  # 초기 우큐 설정
    else:
      hps(queue, (INF, i))

  ijk()

  print(dist[end][0])
  print(len(dist[end][1]))
  print(*dist[end][1])
