import sys
from collections import deque
input = sys.stdin
# BFS
n = int(input.readline().rstrip())
m = int(input.readline().rstrip())
graph = [[] for i in range(n + 1)]
graph[0] = [0, 0]  # dummy
for i in range(m):
    start, end = map(int, input.readline().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향 간선


def BFS(s):
    queue = deque([s])
    check = [0 for i in range(n + 1)]
    cnt = 0
    while queue:
        vertex = queue.popleft()
        for i in (graph[vertex]):
            if not check[i]:
                check[i] = 1
                queue.append(i)
                cnt += 1
    return cnt


print(BFS(1) - 1)  # 1번 컴퓨터는 빼줘야함.
