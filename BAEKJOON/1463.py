import sys
N = int(sys.stdin.readline().rstrip())
dp = [0] * (N + 3); dp[1] = 0; dp[2] = 1; dp[3] = 1
for i in range(4, N + 1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0 and dp[i] > dp[i // 3] :
        dp[i] = dp[i // 3] + 1
    if i % 2 == 0 and dp[i] > dp[i // 2]:
        dp[i] = dp[i // 2] + 1
print(dp[N])

