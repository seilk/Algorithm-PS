import sys

input = sys.stdin.readline
V = int(input().rstrip())
E = int(input().rstrip())
INF = 100000 * 100 + 1 # 비용의 최대값 = 10만 , 도시의 최대값 = 100
graph = [[INF for i in range(V + 1)] for j in range(V + 1)]  # V*V 정방행렬
floyd = [[0] * (V + 1) for i in range(V + 1)]

# 그래프 초기화
for i in range(E):
  start, end, value = map(int, input().split()) # 1 4 10 / 1 4 2 / 1 4 5
  if graph[start][end] == INF:
    graph[start][end] = value
  else:
    graph[start][end] = min(graph[start][end], value)

# 최단거리 행렬 초기화
for i in range(1, V + 1):
  for j in range(1, V + 1):
    # 자기 자신
    if i == j: # 노드 1 -> 노드 1 : 0
      floyd[i][j] = 0
    # 경로가 존재하는 경우
    elif graph[i][j]:
      floyd[i][j] = graph[i][j]
    # 경로가 없는 경우
    else:
      floyd[i][j] = INF

# 경유 노드를 결정하는 for문
for middle in range(1, V + 1):
  # 시작 노드를 결정하는 for문
  for start in range(1, V + 1):
    # 도착 노드를 결정하는 for문
    for end in range(1, V + 1):
      floyd[start][end] = min(floyd[start][middle] + floyd[middle][end], floyd[start][end])

# INF -> 0 보정
for i in range(1, V + 1):
  for j in range(1, V + 1):
    if floyd[i][j] == INF:
      floyd[i][j] = 0

for i in range(1, V + 1):
  print(*floyd[i][1:])
