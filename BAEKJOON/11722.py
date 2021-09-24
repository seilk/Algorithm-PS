import sys
N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(N)]
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if lst[i] > lst[j] :
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
#
