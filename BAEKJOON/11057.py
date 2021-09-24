import sys
N = int(sys.stdin.readline().rstrip())

dp = [[0 for i in range(10)] for i in range(N + 1)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, N + 1):
    dp[i][0] = 1

for i in range(2, N + 1):
    for k in range(1, 10):
        for j in range(0, k + 1):
            dp[i][k] += dp[i - 1][j]
print(sum(dp[N]) % 10007)
#
