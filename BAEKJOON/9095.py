import sys
T = int(sys.stdin.readline().rstrip());
for j in range(T):
    n = int(sys.stdin.readline().rstrip());
    dp = [0] * (n+1000)
    dp[0] = 1; dp[1] = 2; dp[2] = 4;
    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n - 1])


