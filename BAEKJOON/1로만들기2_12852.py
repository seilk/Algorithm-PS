import sys
import time
sys.setrecursionlimit(10 ** 6)
In = lambda: sys.stdin.readline().rstrip()


def solve(N):
	for n in range(1, N + 1):
		for i in range(3):
			if i == 0:
				if n + 1 > N: continue
				if dp[n + 1] > dp[n] + 1:
					dp[n + 1] = dp[n] + 1
					mem[n + 1] = [n + 1] + mem[n]
			if i == 1:
				if n * 2 > N: continue
				if dp[n * 2] > dp[n] + 1:
					dp[n * 2] = dp[n] + 1
					mem[n * 2] = [n * 2] + mem[n]
			else:
				if n * 3 > N: continue
				if dp[n * 3] > dp[n] + 1:
					dp[n * 3] = dp[n] + 1
					mem[n * 3] = [n * 3] + mem[n]

N = int(In())
dp = [1e6 + 9] * (N + 1)
dp[1] = 0
mem = [[] for i in range(N + 1)]
mem[1] = [1]
solve(N)
print(dp[N])
print(*mem[N])