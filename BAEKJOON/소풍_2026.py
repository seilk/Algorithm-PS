# 그래프를 완성시키고 노드를 loop 하며 그 node와 연결된 edge가 k-1인지 확인
import sys

input = sys.stdin.readline
K, N, F = map(int, input().split())
graph = [[i] for i in range(0, N + 1)]
visited = [[0 for i in range(0, N + 1)] for j in range(0, N + 1)]
for i in range(F):
  x, y = map(int, input().split())
  if visited[x][y] == 0:
    graph[x].append(y)
    visited[x][y] = 1
  if visited[y][x] == 0:
    graph[y].append(x)
    visited[y][x] = 1


def DFS(x):
  global flgg
  if flgg:
    return
  if len(ans) == K:
    print(*ans, sep="\n")
    flgg = True
    return
  for i in range(x, N + 1):
    if not visited[i]:
      if ans:
        flg = True
        for j in range(len(ans)):
          if not (ans[j] in graph[i]):
            flg = False
            break
        if flg:
          ans.append(i)
          visited[i] = 1
          DFS(i)
          if not flgg:
            visited[i] = 0
            ans.pop()
  return None
for i in range(1, N + 1):
  ans = [i]
  visited = [0 for i in range(N + 1)]
  visited[i] = 1
  flgg = False
  DFS(i)
  if flgg:
    break
if not flgg:
  print(-1)
