import sys
from collections import deque

input = sys.stdin
n, m, v = map(int, input.readline().split())  # n은 node의 개수, m은 간선의 개수, v는 시작점

# graph 만들기
graph = [
    [] for i in range(n + 1)
]  # n + 1개 행의 list 만듦, 각 행의 idx는 시작점, 각 열은 각 행에서 시작해 끝나는점
pairSet = []
for i in range(m):
    pairSet.append(tuple(map(int, input.readline().split())))  # 문제에서 주어지는 pair를 저장

for ogn, dtn in pairSet:  # pariSet = [(origin, destination), ...]
    graph[ogn].append(dtn)
    graph[dtn].append(ogn)

for i in graph:
    i.sort()  # 오름차순으로 정점을 다녀와야 하므로 각 행의 items를 정렬

check = [0 for i in range(n + 1)]  # 다녀왔다는 check
check[0] = 1

dfsEntry = [v]  # 시작값 고정


def dfs(depth, node):
    check[node] = 1
    if depth == n:
        return
    for i in graph[node]:
        if not check[i]:
            dfsEntry.append(i)
            dfs(depth + 1, i)  # node를 가지고 재귀함수
    return dfsEntry


bfsEntry = [v]


def bfs(queue):  # startingPoint == v
    check[queue[0]] = 1
    while queue:  # 다 방문했으면 while문 종료
        node = queue.popleft()
        for i in graph[node]:  # 시작점 or node와 연결된 node를 먼저 방문함.
            if not check[i]:
                queue.append(i)
                bfsEntry.append(i)
                check[i] = 1
    return bfsEntry


print(*dfs(1, v), sep=" ")  # 시작값을 넣어주므로 depth = 1부터 시작
check = [0 for i in range(n + 1)]
check[0] = 1  # check 초기화
print(*bfs(deque([v])), sep=" ")
