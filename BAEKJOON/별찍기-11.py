import sys

input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
bd = [[" "] * (2 * N - 1) for i in range(N)]
sys.setrecursionlimit(10 ** 8)


def DQ(N, r, c):
  if N == 3:
    bd[r][c], bd[r][c + 1], bd[r][c + 2], bd[r][c + 3], bd[r][c + 4] = "*", "*", "*", "*", "*"
    bd[r - 1][c + 1], bd[r - 1][c + 3], bd[r - 2][c + 2] = "*", "*", "*"
    return
  DQ(N // 2, r, c)
  DQ(N // 2, r, c + N)
  DQ(N // 2, r - N // 2, c + N // 2)


DQ(N, N - 1, 0)
s = ""
for i in range(N):
  if i < N:
    a = "".join(bd[i])
    s += a + "\n"
  else:
    s += "".join(bd[i])

print(s)
