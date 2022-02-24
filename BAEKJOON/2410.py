import sys

input = sys.stdin
n = int(input.readline().rstrip())
dp = [0 for i in range(n + 1)]
dp[0] = 1
powSet = [2 ** x for x in range(21)]  # 2**20이 2의 제곱중에서 처음으로 10**6을 넘는 수
# print(powSet)
for number in powSet:
    if number <= n:
        for idx in range(number, n + 1):
            dp[idx] += dp[idx - number]

print(dp[n] % 1_000_000_000)
