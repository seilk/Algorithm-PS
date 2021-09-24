import sys
n = int(sys.stdin.readline().rstrip())
wine = [0 for i in range(n + 1)]
dp = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    wine[i] = int(sys.stdin.readline().rstrip())

dp[1] = wine[1]

# n = 1 이면 dp[2]가 존재하지 않으므로 indexError 발생
if n >=2 :
    dp[2] = wine[2] + wine[1]

# n = 2 이면 dp[3]가 존재하지 않으므로 indexError 발생
if n >= 3:
    for i in range(3, n+1):
        dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3],
            wine[i] + dp[i - 2], dp[i - 1])
print(dp[n])