from sys import stdin

t = int(stdin.readline().rstrip())
for i in range(t):
    num = int(stdin.readline().rstrip())
    dp = [[0, 0] for _ in range(num + 1)]
    dp[0] = [1, 0]
    if num > 0:
        dp[1] = [0, 1]
    for j in range(2, num + 1):
        dp[j][0] = dp[j - 1][0] + dp[j - 2][0]
        dp[j][1] = dp[j - 1][1] + dp[j - 2][1]
    print(*dp[num], sep=" ")
