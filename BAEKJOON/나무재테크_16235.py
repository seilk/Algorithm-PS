import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


def spring_summer(trees, field, n):
  for row in range(1, n + 1):
    for col in range(1, n + 1):
      l = len(trees[row][col])
      for idx in range(l):
        old = trees[row][col][idx]
        if field[row][col] >= old:
          field[row][col] -= old
          trees[row][col][idx] += 1
        else:
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

for i in range(y):
  spring_summer(trees, field, n)
  autumn_winter(trees, n, extra)


ans = 0
for row in range(1, n + 1):
  for col in range(1, n + 1):
    ans += len(trees[row][col])
print(ans)

# from collections import deque

# a = [[deque([1, 2, 3]) for _ in range(3)] for _ in range(3)]
# for i in range(3):
#   for j in range(3):
#     for z in a[i][j]:
#       print(z, end = " ")
#       if j + 1 < 3:
#         a[i][j + 1].appendleft(0)
#     print()
# for i in range(3):
#   print(*a[i])
