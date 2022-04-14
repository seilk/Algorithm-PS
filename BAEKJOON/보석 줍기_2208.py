import sys

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())

N, M = MIS()
jew = []
prefix = [0] * (N + 1)
for n in range(N):
	jew.append(int(In()))
	prefix[n + 1] = prefix[n] + jew[n]

prefix = prefix[1:]
left = 0
right = M - 1
dp = [0] * N
dp[M-1] = prefix[M-1]  # 1~M 번째 보석을 전부 줍는 경우 (초기화)
for i in range(M, N): # M+1 번째 보석부터 시작
	dp[i] = max(dp[i - 1] + jew[i], prefix[i] - prefix[i - M])

print(max(0, max(dp)))