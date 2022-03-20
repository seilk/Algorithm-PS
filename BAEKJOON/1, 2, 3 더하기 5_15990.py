import sys

In = lambda: sys.stdin.readline().rstrip()
T = int(In())
dp = [[0] * (4) for i in range(100_001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]
MAX = int(1e9 + 9)
for i in range(4, 100_001):
	for j in range(1, 4):
		if j == 1:
			dp[i][1] = (dp[i - j][2] + dp[i - j][3]) % MAX
		if j == 2:
			dp[i][2] = (dp[i - j][1] + dp[i - j][3]) % MAX
		if j == 3:
			dp[i][3] = (dp[i - j][1] + dp[i - j][2]) % MAX

for t in range(T):
	print(sum(dp[int(In())]) % MAX)