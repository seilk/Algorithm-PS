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


#
input = sys.stdin
n, k = map(int, input.readline().split())
obj = [list(map(int, input.readline().split())) for i in range(n)]
obj.insert(0, [0, 0])
dp = [[0 for i in range(k + 1)] for i in range(n + 1)]  # 매 순간 가치의 최댓값
for i in range(1, n + 1):
  for j in range(1, k + 1):
    weight = obj[i][0]
    value = obj[i][1]
    if weight > j:
      dp[i][j] = dp[i - 1][j]
    else:  # weight <= j :
      dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
print(dp[n][k])
