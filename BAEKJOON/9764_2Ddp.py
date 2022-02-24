# ----------Title
# 서로 다른 자연수의 합
# Silver I
# https://boj.kr/9764

# ----------Tip
# DP(2D)
#

# ----------URLs

# ----------Code with Detail
import sys


def input() -> int:
  return int(sys.stdin.readline().rstrip())


t = input()
for i in range(t):
  n = input()
  dp = [[0 for i in range(n + 1)] for i in range(n)]
  dp = [[1 for i in range(n + 1)]] + dp
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      dp[x][y] = dp[x][y - 1] + dp[x - y][y - 1]
  print(dp[n][n] % 100999)
###############################################################
# def boj9764():
#   cnt = 0
#    if t == 1 or t == 2:
#         return print(1)
#     elif t == 3:
#         return print(2)
#     for i in range(2, t // 2):
#         lst = [_ for _ in range(1, t + 1)]
#         comb = combinations(lst, i)
#         for i in comb:
#             if sum(i) == t:
#                 cnt += 1
#     return print(cnt + 1)
# boj9764()
###############################################################
# dp = [[0 for i in range(t + 1)] for i in range(t + 1)]
# if __name__ == "__main__":
#     for n in lst:
#         dp = [0 for i in range(n + 1)]
#         dp[1] = 1  # base
#         dp[2] = 1  # base
#         dp[3] = 2  # base
#         for m in range(4, n + 1):
#             dp[m] = dp[m - 1] + 1
#         print(dp[n] % 100999)
