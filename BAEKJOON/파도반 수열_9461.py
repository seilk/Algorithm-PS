import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

T = int(In())
for t in range(T):
	N = int(In())
	dp = [0] * (101)
	dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
	if N < 6:
		print(dp[N])
		continue
	for n in range(6, N+1):
		dp[n] = dp[n-5] + dp[n-1]
	print(dp[N])
# 1 1 1 2 2 3 4 5 7 9
