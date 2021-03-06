from sys import stdin

n, s = map(int, stdin.readline().split())
series = list(map(int, stdin.readline().split()))
dp = [[] for i in range(n)]
count = 0
if series[0] == s:
    count += 1
dp[0].append(series[0])

for i in range(1, n):
    if series[i] == s:
        count += 1
    dp[i].append(series[i])

    for j in dp[i - 1]:
        dp[i].append(j)

    for j in dp[i - 1]:
        if j + series[i] == s:
            count += 1
        dp[i].append(j + series[i])

print(count)
