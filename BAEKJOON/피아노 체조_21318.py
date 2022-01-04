# ----------Title
# 피아노 체조
# Silver I
# https://www.acmicpc.net/problem/21318

# ----------Tip
# 누적합

# ----------URLs
#

# ----------Code with Detail
import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
level = [0] + list(map(int, input().split()))
check = [0 for i in range(N + 1)]

for i in range(1, N + 1):
  if i == N:
    check[i] = check[i - 1]
  elif level[i] > level[i + 1]:
    check[i] = check[i - 1] + 1
  else:
    check[i] = check[i - 1]
# [0 0 0 0 0 0 1 1 2 3 3]
Q = int(input().rstrip())
for i in range(Q):
  st, ed = map(int, input().split())
  # 현재 악보가 더 어려우면 실수함
  if ed - st == 1:
    miss = check[st] - check[st - 1]
  elif ed == st:
    miss = 0
  else:
    miss = (check[ed - 1] - check[st]) + (check[st] - check[st-1])
  print(miss)
