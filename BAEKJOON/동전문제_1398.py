# ----------Title
# 동전문제
# Gold I
# https://boj.kr/1398

# ----------Tip
# DP
# '동전'의 심화버전
# 규칙성 찾기
# 최소 dp

# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline
tc = int(input().rstrip())

for _ in range(tc):
  n = int(input().rstrip())
  dp = [i for i in range(100)]
  dp[0] = 0
  for i in range(1, 10):
    dp[i] = i
  for i in range(10, 100):
    for coin in [10, 25]:
      if i >= coin:
        dp[i] = min(dp[i], dp[i - coin] + 1)
      # dp[i] = min(dp[i], (i // coin) + dp[i % coin]) #Greedy X

  ans = 0
  while n > 0:
    ans += dp[n % 100]
    n //= 100
  print(ans)
  
  # [1, 10, 25] 5
  # [100, 1000, 2500] 500
  # 59 = 25 * 1 + 10 * 3 + 1 * 4