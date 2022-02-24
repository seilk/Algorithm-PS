import sys
N = int(sys.stdin.readline().rstrip())
dp = [[0 for i in range(2)] for i in range(N + 1)]
dp[1] = [0, 1]
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]
print(sum(dp[N]))