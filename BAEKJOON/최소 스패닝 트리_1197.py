# ----------Title
# 최소 스패닝 트리
# Gold IV
# https://www.acmicpc.net/problem/1197

# ----------Tip
# Prim Algorithm
#

# ----------URLs
# https://bowbowbow.tistory.com/26
# https://stackoverflow.com/questions/52837737/heapify-python-method-in-a-list-of-tuples/52838885

# ----------Code with Detail
from sys import stdin
import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write


def solve():
  ans = 0
  while pq:
    w, f = heapq.heappop(pq)  # weight이 낮은 최소 힙 pop
    if not visited[f]:
      ans += w  # 정답 갱신
      visited[f] = 1
      for t, w in graph[f]:  # index : vertex
        if not visited[t]:  # 방문하지 않은 vertex에 한해서
          heapq.heappush(pq, (w, t))  # weight : graph[from][to]
  print(str(ans))


if __name__ == "__main__":
  # Setting
  v, e = map(int, input().split())
  visited = [0] * (v + 1)
  graph = [[] * (v + 1) for i in range(v + 1)]
  for i in range(1, e+1):
    f, t, w = map(int, input().split())  # from, to, weight
    graph[f].append((t, w))
    graph[t].append((f, w))

  pq = []  # priority queue
  heapq.heappush(pq, (0, 1))  # change list into heap, (weight, node(1~n))
  solve()

# ----------UnionFind 풀이
read = stdin.readline
V, S = map(int, read().split())

edge = []
for _ in range(S):
  a, b, w = map(int, read().split())
  edge.append((w, a, b))

edge.sort(key=lambda x: x[0])

parent = list(range(V + 1))


def union(a, b):
  a = find(a)
  b = find(b)

  if b < a:
    parent[a] = b
  else:
    parent[b] = a


def find(a):
  if a == parent[a]:
    return a
  parent[a] = find(parent[a])  # 경로 압축
  return parent[a]


sum = 0
for w, s, e in edge:
  if find(s) != find(e):
    union(s, e)
    sum += w

print(sum)
