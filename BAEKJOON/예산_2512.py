import sys

input = sys.stdin.readline
N = int(input().rstrip())
arr = [*map(int, input().split())]
T = int(input().rstrip())
arr.sort()
MAX = arr[-1]
MIN = 1
flg = False
while MIN <= MAX and not flg:
  MID = (MIN + MAX) // 2
  SUM = 0
  for v in arr:
    if v > MID:
      SUM += MID
    else:
      SUM += v
  if SUM > T:
    MAX = MID - 1
  elif SUM == T:
    print(MID)
    flg = True
    break
  else:
    MIN = MID + 1
if not flg:
  print(MAX)