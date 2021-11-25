import sys
def input(): return sys.stdin.readline().rstrip()

#DP + BitMask Field
#dp[idx_x][idx_y]
#dp[bitmask]
#dp[0000][cur]
#dp[0001][cur]
#dp[0010][cur]
#...
#dp[1110][2] : cur에서 0번째 도시를 거치고 0번째 도시를 가지 않은상태 0번째도시에서 출발도시로 다시 돌아가는 최소 value
# 2 -> 0 -> 출발도시 의 최소값
#dp[1111][cur]
# 0 1 2 3
# 1 -> 3 -> 2 -> 0 -> 1
# 3 -> 2 -> 0 -> 1 -> 3
# 2 -> 0 -> 1 -> 3 -> 2
# 0

cities = int(input())
graph = [list(map(int, input().split())) for i in range(cities)]
cache = [[-1] * cities for i in range(1 << cities)]

#cache[1111][3] 0 -> 1 -> 2 -> 3 -> 0 return 8
#cache[0111]
#cache[0011]
def DFS(status, current): #<-> BFS, DFS
  if status == (1 << cities) - 1:  # 1111...1111
    if graph[current][0] != 0: # graph[3][0]
      return graph[current][0]  # 마지막으로 현재위치에서 0(출발점)까지 돌아가는 거리 합산
    return float("inf")  # 경로가 없으면 INF return

  if cache[status][current] != -1:  # cache에 저장된 값이 존재할 때 (memo 활용)
    return cache[status][current]

  cache[status][current] = float("inf")  # for문 안에서 min값 비교를 위한 initiallization
  for i in range(cities):
    if status & (1 << i) == 0 and graph[current][i] != 0:
      cache[status][current] = min(cache[status][current], DFS(
          status | (1 << i), i) + graph[current][i])
      # if not visited[i]:
      #   visited[i] = 1
  return cache[status][current]


# 0 > 1 > 2
# cache[]
# cache[7][2] = 20 -> cache[0111][2] = 20 -> 2번째 도시에서 3번째도시를 거쳐서 0번째 도시로 돌아가는 경로의 최소값
# cache[0011][1] = 1번째도시에서 2번째도시와 3번째 도시를 거쳐서 0번째 도시로 돌아가는 경로의 최소값
# cache[i][j] = 이미 방문한 도시들의 집합이 i (0011) 이고 현재 있는 도시가 j일때, 방문하지 않은 나머지 도시들을 모두 방문한 뒤 출발 도시로 돌아올 때 드는 최소 비용.
# cache[1011] cache[0111] 
# cache[00111][c]

DFS(1, 0)  # -> (0001, 0)
# for i in range(len(cache)):
#   print(*cache[i])
print(min(i for i in cache[1] if i > -1))

# 0001 -> 0011 -> 0111 -> 1111(15) -> 3
# &
# 1 << 0 = 1, 0001 & 1 = 1
# 1 << 1 = 10, 0001 & 10 = 0
# 1 << 2 = 100, 0001 &
# 1 << 3 = 1000

#cache[0001][0], cache[0001][1], cache[0001][2] cache[0001][3]
# inf, 0 -> "1"(Current)
# cache[0001]

# cache[1101][2] : 현재위치 (2)에서 1번째도시 (비어있는 도시)를 가서 시작도시로 순회하는 최소비용
# cache[0011][1] : 현재위치 1/ 2번째 3번째 돌고/ 시작도시 순회 최소비용
# cache[0001][1] : 1 -> pass
