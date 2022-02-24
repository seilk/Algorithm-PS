# ----------Title
# 평범한 배낭
# Gold V
# https://www.acmicpc.net/problem/12865


# ----------Tip
# Knapsack DP

# ----------URLs
# https://hongcoding.tistory.com/50


# ----------Code with Detail
import sys
input = sys.stdin.readline
n, k = map(int, input().split()) 
infos = [(0, 0)] + [tuple(map(int, input().split())) for i in range(n)]
dp = [[0]*(k + 1) for i in range(n + 1)]
for i in range(1, n):
  for j in range(1, k + 1):
    if infos[i][0] <= j:
      dp[i][j] = max(dp[i][j - infos[i][0]] + infos[i][1], dp[i - 1][j])
    else:
      dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[n][k])