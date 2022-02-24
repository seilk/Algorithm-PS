import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input().rstrip())
arr = [[" " for i in range(n)] for j in range(n)]


def rec(lc, k):
  l0, l1 = lc
  if k == 3:
    arr[l0][l1] = "*"
    arr[l0][l1 + 1] = "*"
    arr[l0][l1 + 2] = "*"

    arr[l0 + 1][l1] = "*"
    arr[l0 + 1][l1 + 1] = " "  # 공백
    arr[l0 + 1][l1 + 2] = "*"

    arr[l0 + 2][l1] = "*"
    arr[l0 + 2][l1 + 1] = "*"
    arr[l0 + 2][l1 + 2] = "*"
    return

  else:
    a = k//3
    b = (k//3) * 2

    rec((l0, l1), k//3)  # 1
    rec((l0, l1 + a), k//3)  # 2
    rec((l0, l1 + b), k//3)  # 3

    rec((l0 + a, l1), k//3)  # 4

    rec((l0 + a, l1 + b), k//3)  # 6

    rec((l0 + b, l1), k//3)  # 7
    rec((l0 + b, l1 + a), k//3)  # 8
    rec((l0 + b, l1 + b), k//3)  # 9


rec((0, 0), n)
for i in range(n):
  print(*arr[i], sep="")
