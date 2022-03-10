import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline().rstrip())
MOD = 15746
dp = [0] * (1_000_001)
dp[1] = 1; dp[2] = 2
for i in range(3, N+1):
	dp[i] = (dp[i-1]%MOD + dp[i-2]%MOD)%MOD
print(dp[N])


# (A+B)%C = (A%C + B%C)%C

# 1
# 00 11
# 100 111 001
# 0000 1100 / 1001 1111 0011