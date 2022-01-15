import sys
input = sys.stdin.readline
N = int(input().rstrip())
lq = [*map(int, input().split())]
left = 0
right = N - 1
mnn = 2_000_000_001
ans = [1_000_000_001, 1_000_000_001]
while left < right:
  val = lq[left] + lq[right]
  if abs(val) < mnn:
    mnn = abs(val)
    ans = [lq[left], lq[right]]
  if val < 0:
    left += 1
  else:
    right -= 1
print(*ans)