import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    N = int(sys.stdin.readline().rstrip())
    firstRow = list(map(int, sys.stdin.readline().split()))
    secondRow = list(map(int, sys.stdin.readline().split()))
    dp = [firstRow, secondRow]
    if N == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    else :
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for i in range(2, N):
            dp[0][i] = max(dp[1][i - 2] + dp[0][i], dp[1][i - 1] + dp[0][i]) 
            dp[1][i] = max(dp[0][i - 1] + dp[1][i], dp[0][i - 2] + dp[1][i])
        print(max(dp[0][N - 1], dp[1][N - 1]))
