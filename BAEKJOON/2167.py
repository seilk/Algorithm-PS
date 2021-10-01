import sys


def input():
    return sys.stdin.readline()


row, col = map(int, input().split())

b = []
for i in range(row):
    b += [list(map(int, input().split()))]

dp = [[0 for i in range(col + 1)] for i in range(row + 1)]
for i in range(1, row + 1):
    for j in range(1, col + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - \
            dp[i - 1][j - 1] + b[i - 1][j - 1]

k = int(input().rstrip())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])
