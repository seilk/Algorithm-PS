import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

n = int(In())
arr = [None] + [*MIS()]
dp = [0] * (n + 1)

for i in range(1, n + 1):
	for j in range(i, 0, -1):
		mxx = max(arr[j:i+1])
		mnn = min(arr[j:i+1])
		dp[i] = max(dp[i], mxx - mnn + dp[j-1])

print(dp[n])
