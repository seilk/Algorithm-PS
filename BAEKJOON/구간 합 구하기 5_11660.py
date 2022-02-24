import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nms = [[0] * (n + 1)] + [[0] + list(map(int, input().split()))
                         for i in range(n)]
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[1][1] = nms[1][1]
for k in range(2, n + 1):
  dp[k][1] = dp[k - 1][1] + nms[k][1]
  dp[1][k] = dp[1][k - 1] + nms[1][k]

for i in range(2, n + 1):
  for j in range(2, n + 1):
    dp[i][j] = nms[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for c in range(m): #O(m)
  x1, y1, x2, y2 = map(int, input().split())
  print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])
