# ----------Title
# 구간 합 구하기 4
# Silver III
# https://www.acmicpc.net/problem/11659

# ----------Tip
# prefix
# 매번 sum을 구하는 것은 비효율적이다.


# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n, m = map(int, input().split())
nms = [0] + list(map(int, input().split()))
a = 0
localsum = [0] * (n + 1)


def rec(idx):
  if idx == 1:
    localsum[1] = nms[1]
    return localsum[1]
  localsum[idx] = nms[idx] + rec(idx - 1)
  return localsum[idx]


rec(n)

for i in range(m):
  f, t = map(int, input().split())
  print(localsum[t] - localsum[f - 1])
