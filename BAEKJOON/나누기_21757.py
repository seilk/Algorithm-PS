import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
arr = [0] + [*MIS()]
pf = [0, arr[1]]
for i in range(2, N+1):
	pf.append(pf[i-1] + arr[i])
tot = pf[-1] # 전체합

if tot % 4 != 0:
	print(0)
else:
	dp = [[0] * (N+1) for i in range(5)]
	div = [-1, tot//4, tot//2, 3*tot//4, tot] # 각 부분수열 별 합 정보
	for d in range(1, 4):
		for i in range(1,N):
			if pf[i] == div[d]:
				if d == 1:
					dp[d][i] = dp[d][i-1] + 1
					continue
				dp[d][i] = dp[d-1][i-1] + dp[d][i-1]
			else:
				dp[d][i] = dp[d][i-1]
	print(dp[3][N-1])
