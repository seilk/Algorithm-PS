# ----------Title
# 동전
# Gold III
# https://boj.kr/2091

# ----------Tip
# DP
# '동전'의 심화버전
# 최대 DP
# 동전의 개수가 정해져 있음

# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline
x, a, b, c, d = map(int, input().split())

dp = [[-1] * (5) for i in range(x + 1)]  # dp table
coin = [1, 5, 10, 25]
nc = [a, b, c, d]  # coin의 개수
dp[0] = [0, 0, 0, 0, 0]  # 0원을 만드는 각 coin의 개수

for p in range(1, x + 1):
  for c in range(4):
    if dp[p][c] == -1:
      dp[p][c] = 0
    if p >= coin[c]:  # 동전으로 가격을 만들 수 있을 때
      if nc[c] >= dp[p - coin[c]][c] + 1:  # 동전을 사용하는것이 가능할 때
        # 현재 가격을 맞추는데 현재 동전을 쓰는 경우가 쓰지 않는 경우보다 크면
        if dp[p - coin[c]][4] > dp[p][4]:
          # 전체 동전의 개수 갱신
          dp[p][4] = dp[p - coin[c]][4] + 1

          # 동전별 개수 갱신
          for cc in range(4):
            dp[p][cc] = dp[p - coin[c]][cc]

          # 현재 가격에서 현재 동전의 개수 +1
          dp[p][c] += 1

print(*dp[x][:4])

# for i in range(x + 1):
#   print(*dp[i])
# 12 5 3 1 2
# [0] 0 0 0 0 0
# [1] 1 0 0 0 1
# [2] 2 0 0 0 2
# [3] 3 0 0 0 3
# [4] 4 0 0 0 4
# [5] 5 0 0 0 5 (동전: 5원, 현재가격: 5원)
# [6] 1 1 0 0 2
# [7] 2 1 0 0 3
# [8] 3 1 0 0 4
# [9] 4 1 0 0 5
# [10] 5 1 0 0 6
# [11] 1 2 0 0 3
# [12] 2 2 0 0 4
