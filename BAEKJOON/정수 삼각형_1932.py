import sys
input = sys.stdin.readline
n = int(input().rstrip())
tri = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]
dp[0][0] = tri[0][0]
for i in range(1, n):
  for j in range(i + 1):
    dp[i][j] = max(dp[i - 1][j - 1] + tri[i][j], dp[i - 1][j] + tri[i][j])

print(max(dp[-1]))
