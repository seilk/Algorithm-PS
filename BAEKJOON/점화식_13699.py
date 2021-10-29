import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
dp = [0] * (n + 2)
dp[0], dp[1] = 1, 1
for x in range(2, n + 1):
    for i in range(0, x // 2):
        dp[x] += dp[i] * dp[x - 1 - i]
    dp[x] *= 2
    if x & 1:  # x가 홀수일때
        dp[x] += dp[x // 2] ** 2

# 02
# 11
# 20
print(*dp)
print(dp[n])
