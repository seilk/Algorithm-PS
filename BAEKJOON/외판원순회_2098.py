import sys
def input(): return sys.stdin.readline().rstrip()


cities = int(input())
graph = [list(map(int, input().split())) for i in range(cities)]
cache = [[-1] * cities for i in range(1 << cities)]


def DFS(status, current):
  if status == (1 << cities) - 1:  # 1111...1111
    if graph[current][0] != 0:
      return graph[current][0]  # 마지막으로 현재위치에서 0(출발점)까지 돌아가는 거리 합산
    return float("inf")  # 경로가 없으면 INF return

  if cache[status][current] != -1:  # cache에 저장된 값이 존재할 때 (memo 활용)
    return cache[status][current]

  cache[status][current] = float("inf")  # for문 안에서 min값 비교를 위한 initiallization
  for i in range(cities):
    # 현재 도시에서 i번째 도시로 갈 수 있을 때 (아직 방문하지 않은 도시 and 경로가 존재하는 도시)
    if status & (1 << i) == 0 and graph[current][i] != 0:
      cache[status][current] = min(cache[status][current], DFS(
          status | (1 << i), i) + graph[current][i])
  return cache[status][current]


DFS(1, 0)  # (0번째 도시, 0001)
print(min(i for i in cache[1] if i > -1))
