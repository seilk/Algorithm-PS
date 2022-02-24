# ----------Title
# 특정 거리의 도시 찾기
# Silver II
# https://www.acmicpc.net/problem/18352

# ----------Tip
# Dijkstra
#

# ----------URLs
# https://m.blog.naver.com/ndb796/221234424646

# ----------Code with Detail
import sys
from collections import defaultdict, deque


def solve(k):
  ans = []
  while queue:
    dist, node = queue.popleft()  # (dist, node)
    visited[node] = dist

    if dist == k:
      ans.append(node)
      continue

    if dist < k:
      while graph[node]:
        to = graph[node].popleft()
        if visited[to] == -1:  # 아직 방문하지 않은 node인 경우
          visited[to] = dist + 1
          queue.append((dist + 1, to))

  if ans != []:
    ans.sort()
    print(*ans, sep="\n")
  else:
    print(-1)


if __name__ == "__main__":
  # Setting
  input = sys.stdin.readline
  v, e, k, s = map(int, input().split())  # vertex, edges, k, starting
  graph = defaultdict(deque)  # queue를 기본 자료구조형으로 설정
  for _ in range(e):
    frm, to = map(int, input().split())
    graph[frm].append(to)

  queue = deque([(0, s)])  # (weight , node)
  visited = [-1] * (v+1)
  # Build
  solve(k)
