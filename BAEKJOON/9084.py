import sys

input = sys.stdin
t = int(input.readline().rstrip())
for i in range(t):
    numOfCoins = int(input.readline().rstrip())
    coins = list(map(int, input.readline().split()))
    n = int(input.readline().rstrip())
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for coin in coins:
        if coin <= n:
            for idx in range(coin, n + 1):
                dp[idx] += dp[idx - coin]
    print(dp[n])
