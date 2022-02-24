# ----------Title
# 쉬운계단수
# Silver I
# https://boj.kr/10844

# ----------Tip
# DP

# ----------URLs

# ----------Code with Detail

import sys
N = int(sys.stdin.readline().rstrip())
# [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
dp = [[0 for j in range(10)] for i in range(N)]

for i in range(0, 10):
  dp[0][i] = 1

dp[0][0] = 0

for i in range(1, N):
  for j in range(0, 10):
    if j == 0:
      dp[i][j] = dp[i - 1][j + 1]
    if j == 9:
      dp[i][j] = dp[i - 1][j - 1]
    else:
      dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[N-1]) % (10**9))
