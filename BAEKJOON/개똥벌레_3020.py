# ----------Title
# 개똥벌레
# Gold V
# https://boj.kr/3020

# ----------Tip
# 누적합
# Binary Search

# ----------URLs
# https://jaimemin.tistory.com/760

# ----------Code with Detail
import sys

input = sys.stdin.readline
N, H = map(int, input().split())
X = [0 for i in range(H + 1)]
Y = [0 for i in range(H + 1)]
Z = [0 for i in range(H + 1)]
for i in range(1, N + 1):
  if i & 1:
    X[int(input())] += 1  # bottom
  else:
    Y[H - int(input()) + 1] += 1  # top


def sort(lst, foo):
  if foo:  # 종유석(위에서 아래)
    for h in range(1, H + 1):
      lst[h] += lst[h - 1]
  else:  # 석순(아래에서 위)
    for h in range(H - 1, 0, -1):
      lst[h] += lst[h + 1]


sort(X, False)
sort(Y, True)


def tot(X, Y):
  idx = 0
  for x, y in zip(X, Y):
    Z[idx] = x + y
    idx += 1


tot(X, Y)
mn = min(Z[1:])
cnt = Z[1:].count(mn)
print(mn, cnt)

# 4 500000
# 40000
# 40000
# 40000
# 40000
