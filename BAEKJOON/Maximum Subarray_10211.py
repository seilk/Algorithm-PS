# ----------Title
# Maximum Subarray
# Silver III
# https://boj.kr/10211

# ----------Tip
# DP

# ----------URLs

# ----------Code with Detail
import sys
# setrecursionlimit : 10 ** 10 -> overflow error, 1e10 -> Type Error
sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().rstrip()


cases = int(input())
answer = []


def DynamicProgramming(idx, series):  # Top_Down
  if idx == 0:
    return series[idx]
  dp[idx] = max(series[idx], series[idx] + DynamicProgramming(idx - 1, series))
  # 2 1 -2 3 -5
  #dp = [2, 3, 1, 4, -1]
  # i번째 원소의 경우의 수 : 1. 자기 자신이 최대합에 포함되는 경우 2. 포함되지 않는 경우
  return dp[idx]


for i in range(cases):
  size = int(input())  # 5
  series = list(map(int, input().split()))  # [2 1 -2 3 -5]
  dp = [-100_001] * size
  dp[0] = series[0]
  DynamicProgramming(size - 1, series)  # (4, [2 1 -2 3 -5])
  answer.append(max(dp))

print(*answer, sep="\n")
