import sys
from collections import deque


def BFS(GRAPH, i):
  dq = deque([(i, 1)])
  coloring[i] = 1  # color는 1 or -1
  while dq:
    node, color = dq.popleft()
    neighbor = deque(GRAPH[node])
    while neighbor:
      nnode = neighbor.popleft()
      if not coloring[nnode]:
        coloring[nnode] = -color
        dq.append((nnode, -color))
      elif coloring[nnode] == color:  # 인접하는 노드가 같은 색상일 때
        return False
  return True


def solve():
  global coloring
  for i in range(K):
    V, E = map(int, input().split())
    GRAPH = [[] for i in range(V + 1)]
    for e in range(E):
      node1, node2 = map(int, input().split())
      GRAPH[node1].append(node2)
      GRAPH[node2].append(node1)
    coloring = [0] * (V + 1)
    for i in range(1, V + 1): # 불완전그래프 가능성이 있음
      if not coloring[i]:
        FLAG = BFS(GRAPH, i)
        if FLAG == False:
          break
    if FLAG:
      print("YES\n")
    else:
      print("NO\n")


if __name__ == "__main__":
  input = sys.stdin.readline
  print = sys.stdout.write
  K = int(input().rstrip())
  solve()
