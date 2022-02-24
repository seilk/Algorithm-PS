# ----------Title
# 최단경로
# Gold V
# https://www.acmicpc.net/problem/1753


# ----------Tip
# Dijkstra
# Greedy + DP
# 최대한 덜 경유하는 것이 좋다. ; Greedy / 시간복잡도를 줄이기 위해서 이미 구해놓은 최소 값을 이용한다. ; dP
# 최대한 덜 경유하는것이 좋다. : 출발지에서 direct로 갈 수 없는 node들은 출발지에서 direct로 갈 수 있는 node에서 direct로 갈 수 있는 node의 최단거리이다.


# ----------URLs
# https://blog.naver.com/ndb796/221234424646


# ----------Code with Detail
import sys
import heapq


def ijk():
  # 초기 : 시작노드 pop 이후 시작점에서 가까운 순으로 이웃 node 고름
  # 중기 : 시작노드에서 가장 가까운 거리에 있는 (w가 작은) item을 heappop
  # 헷갈릴만한 정보 : queue에는 같은 node이지만 다른 weight를 가진 item이 존재할 수 있다. heappop을 이용해서 거른다.
  while queue:
    weight, node = heapq.heappop(queue)  # 출발지로부터 가장 가까운 노드를 우선적으로 뽑음
    visited[node] = 0  # heappop에 의해 뽑혔다는 것은 더 이상 dist[node]보다 가까운 거리는 없다는 의미
    if dist[node] < weight:  # 저장된 거리보다 weight 자체가 크면 continue, 조건 성립 X
      continue
    for w, t in gp[node]:  # 뽑은 node의 이웃노드 검색
      # if visited[t] == -1:  # 방문 안한 node만
      #   # 이 부분이 Greedy한 과정
      #   # 출발지에서 to 까지의 거리와 경유해서 가는 거리 비교
      #   # 거리 가까우면 우선 heap에 넣고 본다
        if dist[t] > dist[node] + w:
          dist[t] = dist[node] + w  # 초기화
          heapq.heappush(queue, (dist[t], t))


if __name__ == "__main__":
  # Setting
  input = sys.stdin.readline
  INF = 9876543210
  v, e = map(int, input().split())
  s = int(input().rstrip())
  gp = [[]for i in range(v + 1)]
  dist = [-1] * (v + 1)  # 출발지로부터 다른 node의 최소거리; 불가능 = INF
  visited = [-1] * (v + 1)  # 방문 체크
  visited[0] = 0  # 0번 node는 Dummy

  # Graph작성 : 인접리스트
  for i in range(e):
    f, t, w = map(int, input().split())
    gp[f].append((w, t))

  # queue 초기화
  queue = []  # 다익스트라 heap
  for i in range(0, v + 1):
    if i == s:
      heapq.heappush(queue, (0, i))
    else:
      heapq.heappush(queue, (INF, i))

  # dist 초기화
  dist[s] = 0  # 시작점에서 시작점까지의 거리 = 0
  for i in range(v + 1):
    if dist[i] == -1:
      dist[i] = INF

  ijk()  # Dijkstra Solve

  # print
  for d in dist[1:]:
    print("INF") if d == INF else print(d)
