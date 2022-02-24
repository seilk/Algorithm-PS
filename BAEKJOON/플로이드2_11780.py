import sys
input = sys.stdin.readline
V = int(input().rstrip())
E = int(input().rstrip())
INF = float("inf")
graph = [[INF for i in range(V + 1)] for j in range(V + 1)]  # V*V 정방행렬
floyd = [[0] * (V + 1) for i in range(V + 1)]
floyd_route = [[i] * (V + 1) for i in range(V + 1)]
# route 초기화
for i in range(0, V + 1):
  for j in range(0, V + 1):
    floyd_route[i][j] = [i]

# 그래프 초기화
for i in range(E):
  start, end, value = map(int, input().split())
  if graph[start][end] == INF:
    graph[start][end] = value
  else:
    graph[start][end] = min(graph[start][end], value)

# 최단거리 행렬 초기화
for i in range(1, V + 1):
  for j in range(1, V + 1):
    # 자기 자신
    if i == j:
      floyd[i][j] = 0
    # 경로가 존재하는 경우
    elif graph[i][j] < INF:
      floyd[i][j] = graph[i][j]
      floyd_route[i][j] = [i, j]
    # 경로가 없는 경우
    else:
      floyd[i][j] = INF

# 경유 노드를 결정하는 for문
for middle in range(1, V + 1):
  # 시작 노드를 결정하는 for문
  for start in range(1, V + 1):
    # 도착 노드를 결정하는 for문
    for end in range(1, V + 1):
      if floyd[start][middle] + floyd[middle][end] < floyd[start][end]: #거쳐가는 경우가 더 짧은 경우
        floyd[start][end] = floyd[start][middle] + floyd[middle][end]
        floyd_route[start][end] = floyd_route[start][middle] + floyd_route[middle][end][1:]

# INF -> 0 보정
for i in range(1, V + 1):
  for j in range(1, V + 1):
    if floyd[i][j] == INF:
      floyd[i][j] = 0

for i in range(1, V + 1):
  print(*floyd[i][1:])

for i in range(1, V + 1):
  for j in range(1, V + 1):
    if len(floyd_route[i][j]) > 1:
      print(len(floyd_route[i][j]), end=" ")
      print(*floyd_route[i][j])
    else:
      print(0)
'''
0 1 1 0 
1 0 2 0 
2 1 0 0 
0 0 0 0 
0
2 1 2
2 1 3
0
2 2 1
0
3 2 1 3
0
3 3 2 1
2 3 2
0
0
0
0
0
0
'''