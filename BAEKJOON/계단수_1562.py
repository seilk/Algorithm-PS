# ----------Title
# 계단수
# Gold I
# https://boj.kr/1562

# ----------Tip
# DP
# 쉬운 계단 수에 어떤 숫자가 쓰였는지 마킹하는것만 추가된 문제
# 숫자 마킹은 BitMask로...

# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [[[0] * 1025 for j in range(10)] for k in range(n + 1)]

# 기본값 Setting
for c in range(1, 10):  # 그냥 숫자 0 은 계단수 아님 주의
  dp[1][c][1 << c] = 1

for r in range(2, n + 1):
  for c in range(10):
    for b in range((2 ** 10)):  # 0 ~ 111...111
      if c == 0:
        dp[r][c][(1 << c) | b] += dp[r - 1][c + 1][b]  # 누적합

      if 0 < c < 9:
        dp[r][c][(1 << c) | b] += dp[r - 1][c - 1][b] + dp[r - 1][c + 1][b]

      if c == 9:
        dp[r][c][(1 << c) | b] += dp[r - 1][c - 1][b]

if __name__ == "__main__":
  ans = 0
  MOD = 1_000_000_000 
  for c in range(10):  # n의 자리수 구하기
    ans = (ans + dp[n][c][1023]) % MOD  # 111...111 = 1023
  print(ans)

# 32
