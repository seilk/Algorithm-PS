import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
vals = []
for _ in range(n):
	vals.append(int(sys.stdin.readline().rstrip()))
dp = [100_001] * (k + 1)
dp[0] = 0
for i in range(1, k+1):
	for j in range(n):
		if i >= vals[j]:
			dp[i] = min(dp[i], dp[i-vals[j]] + 1)
print(dp[k] if dp[k] != 100_001 else -1)