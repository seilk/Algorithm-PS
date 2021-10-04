# 5
# -1 0 0 1 1
# 2


# 0 1 2
# 1 3 4
# 2
# 3
# 4

# 9
# -1 0 0 2 2 4 4 6 6
# 4

# 0 1 2
# 1
# 2 3 4
# 3
# //4 5 6
# //5
# //6 7 8
# //7
# //8

# 0 1
# 1 2,3 -> []
# #2 3
# #3

from collections import deque
import sys


def input():
    return sys.stdin.readline()


nodes = int(input().rstrip())
graph = [[] for i in range(nodes)]
info = list(map(int, input().split()))

for i in range(nodes):
    if info[i] == -1:
        root = i
        continue
    graph[info[i]].append(i)

delete = int(input().rstrip())
if delete == root:
    print(0)
    sys.exit()
queue = deque([delete])
dSet = {delete}
while queue:
    d = queue.popleft()
    for i in graph[d]:
        queue.append(i)
        dSet.add(i)
    graph[d] = 0

for i in range(nodes):
    if graph[i] == [delete]:
        graph[i] = []

print(graph.count([]))
