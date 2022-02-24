# ----------Title
# 지름길
# Silver I
# https://www.acmicpc.net/problem/1446

# ----------Tip
# DP
# 시간복잡도 = O(V^2 + V)

# ----------URLs


# ----------Code with Detail
import sys
from collections import deque
input = sys.stdin.readline


def solve():
  while nodes:  # V
    node = nodes.popleft()
    if node > d:  # 150까지만 가면 되는데 151
      break
    if way[node] != []:  # 지름길이 존재할 때 탐색
      for dist, frm in way[node]:  # V - 1
        dp[node] = min(dp[node], dist + dp[frm])

    for frm in pre:  # V
      dp[node] = min(dp[node], dp[frm] + node - frm)
    sys.stdout.write(str(node) + "'s short dist is " + str(dp[node]) + "\n")
    pre.append(node)
  print(dp[d])


if __name__ == "__main__":
  # Setting
  n, d = map(int, input().split())
  way = [[] for i in range(10001)]  # 지름길 저장
  nodes = {d}  # 종점
  for i in range(n):
    f, t, dist = map(int, input().split())
    way[t].append((dist, f))  # t0 index에 (거리, from) 저장
    nodes.add(t)
    nodes.add(f)
  dp = [i for i in range(10001)]  # 최소값 초기화 # 0번째 ~ i번째
  nodes = deque(sorted(list(nodes)))
  pre = [nodes.popleft()]  # 시작점 pre

  # Build
  solve()
