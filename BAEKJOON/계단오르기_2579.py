# ----------Title
# 계단 오르기
# Silver I
# https://www.acmicpc.net/problem/2579

# ----------Tip
# DP
# Top-Down 오기 부리지 말자

# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline


def solve():  # Bottom-Up
  for i in range(2, n + 1):
    for j in range(i - 2, i):
      if j == i - 1:
        if j == 1:
          dp[i][0] = max(dp[j]) + ss[i]
          continue
        dp[i][0] = dp[j][1] + ss[i]
      else:
        dp[i][1] = max(dp[j]) + ss[i]
  print(max(dp[n]))


if __name__ == "__main__":
  n = int(input().rstrip())
  ss = [0] + [int(input().rstrip()) for i in range(n)]
  dp = [[0, 0]] + [[-1, -1] for i in range(n)]
  dp[1] = [ss[1], 0]
  solve()
