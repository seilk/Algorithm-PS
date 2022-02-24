# ----------Title
# 동전
# Gold V
# https://www.acmicpc.net/problem/9084


# ----------Tip
# Knapsack DP

# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline
t = int(input().rstrip())
for i in range(t):
  numOfCoins = int(input().rstrip())
  coins = list(map(int, input().split()))
  n = int(input().rstrip())

  dp = [0 for i in range(n + 1)]
  dp[0] = 1
  for coin in coins:
    if coin <= n:
      for target in range(coin, n + 1):
        dp[target] += dp[target - coin]
  print(dp[n])


# 10 1 2
#999 + 1
  #998 + 1
  #997 + 2

#998 + 2
  #997 + 1
  #996 + 2
