import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N, K = MIS()
coins = [int(In()) for i in range(N)]
dp = [0] * (K+1)
dp[0] = 1
for c in coins:
	for v in range(1, K+1):
		if v >= c:
			dp[v] += dp[v - c]
	

print(dp[K])
# 1
# 11 2
# 111 21