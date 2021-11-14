import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
series = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = series[0]


def BS(mn, mx, target):
  while mn < mx:
    mid = (mn + mx) // 2
    if dp[mid] < target:
      mn = mid + 1
    else:
      mx = mid
  return mn


size = 1
for i in range(1, n):
  if dp[size] < series[i]:
    size += 1
    dp[size] = series[i]
  else:
    idx = BS(1, size, series[i])
    dp[idx] = series[i]

print(size)

