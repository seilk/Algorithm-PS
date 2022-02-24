# ----------Title
# 네트워크 연결
# Gold IV
# https://www.acmicpc.net/problem/1922

# ----------Tip
# Prim Algorithm / MST
# 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라.
#

# ----------URLs
# https://bowbowbow.tistory.com/26
# https://stackoverflow.com/questions/52837737/heapify-python-method-in-a-list-of-tuples/52838885

# ----------Code with Detail
import sys
import heapq
input = sys.stdin.readline


def MST():  # prim algorithm
  global ans
  while queue:
    w, t = heapq.heappop(queue)
    if not visited[t]:
      ans += w
      visited[t] = 1
      for wt, to in grp[t]:
        if not visited[to]:
          heapq.heappush(queue, (wt, to))
  print(ans)


if __name__ == "__main__":
  v = int(input().rstrip())
  e = int(input().rstrip())

  grp = [[] for i in range(v + 1)]
  for _ in range(e):
    f, t, w = map(int, input().split())
    grp[f].append((w, t))  # 양방향
    grp[t].append((w, f))

  queue = []
  visited = [0] * (v + 1)
  heapq.heappush(queue, (0, 1))  # 초기값 세팅

  ans = 0
  MST()
