import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


def spring_summer(trees, field, n):
  for row in range(1, n + 1):
    for col in range(1, n + 1):
      l = len(trees[row][col])
      for idx in range(l):
        old = trees[row][col][idx]
        if field[row][col] >= old:  # 나무가 생존
          field[row][col] -= old
          trees[row][col][idx] += 1

        else:  # 나무가 사망
          for k in range(idx, len(trees[row][col])):
            soil = trees[row][col].pop()
            field[row][col] += soil//2
          break


def autumn_winter(trees, n, extra):
  for row in range(1, n + 1):
    for col in range(1, n + 1):
      for old in trees[row][col]:
        if not (old % 5):
          for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                         (0, 1), (1, -1), (1, 0), (1, 1)]:
            if 1 <= row + dr < n + 1 \
                    and 1 <= col + dc < n + 1:
              nrow, ncol = row + dr, col + dc
              trees[nrow][ncol].appendleft(1)
      field[row][col] += extra[row][col]


# 기본세팅
n, t, y = map(int, input().split())
trees = [[0] * (n + 1)] + [[0] + [deque() for i in range(n)] for i in range(n)]
field = [[0] * (n + 1)] + [[0] + [5] * n for i in range(n)]
extra = [[0] * (n + 1)] + [[0] + list(map(int, input().split()))
                           for i in range(n)]
deadtrees = [[0] * (n + 1)] + [[0] + [[] for i in range(n)] for i in range(n)]
flag = False

for tree_info in range(t):
  row, col, old = map(int, input().split())
  trees[row][col].append(old)


# main
for i in range(y):
  spring_summer(trees, field, n)
  autumn_winter(trees, n, extra)


ans = 0
for row in range(1, n + 1):
  for col in range(1, n + 1):
    ans += len(trees[row][col])
print(ans)
