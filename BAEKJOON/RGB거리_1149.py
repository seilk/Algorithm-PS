import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))
dp = [[0 for i in range(3)] for i in range(n)]
dp[0] = rgb[0].copy()
#
for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1] + rgb[i][j], dp[i - 1][2] + rgb[i][j])
        if j == 1:
            dp[i][j] = min(dp[i - 1][0] + rgb[i][j], dp[i - 1][2] + rgb[i][j])
        if j == 2:
            dp[i][j] = min(dp[i - 1][0] + rgb[i][j], dp[i - 1][1] + rgb[i][j])

# for i in range(n):
#     print(*dp[i])
print(min(dp[n - 1]))
