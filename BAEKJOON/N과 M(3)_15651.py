# ----------Title
# N과M(3)
# Silver III
# https://www.acmicpc.net/problem/15651

# ----------Tip
# BackTracking


# ----------URLs


# ----------Code with Detail
import sys


def DFS(cnt, ans, n, m):
  if cnt == m:
    print(*ans)
    return
  for i in range(1, n + 1):
    DFS(cnt + 1, ans + [i], n, m)


if __name__ == "__main__":
  input = sys.stdin.readline
  n, m = map(int, input().split())
  lst = [i for i in range(0, n + 1)]
  DFS(0, [], n, m)
