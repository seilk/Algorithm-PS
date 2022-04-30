import sys

In = lambda : sys.stdin.readline().rstrip()

n = int(In())
MOD = 9901

dp = [[0]*3 for i in range(n)]
dp[0][0], dp[0][1], dp[0][2] = 1, 1, 1

for i in range(1, n) :
	for j in range(3) :
		if j == 0 :
			dp[i][j] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%MOD
		if j == 1 :
			dp[i][j] = (dp[i-1][0]+dp[i-1][2])%MOD
		if j == 2 :
			dp[i][j] = (dp[i-1][0]+dp[i-1][1])%MOD

print(sum(dp[n-1])%MOD)
