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
  return dp[idx]


for i in range(cases):
  size = int(input())
  series = list(map(int, input().split()))
  dp = [-100_001] * size
  dp[0] = series[0]
  DynamicProgramming(size - 1, series)
  answer.append(max(dp))

print(*answer, sep="\n")
