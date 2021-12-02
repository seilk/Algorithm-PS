import sys
input = sys.stdin.readline
n, m = map(int, input().split())
srs = [0] + [i for i in range(1, n + 1)]
visited = [0] * (n + 1)
ans = []


def DFS(d):
  if d == m:
    print(*ans)
    return

  for i in range(1, n+1):
    if ans:
      if srs[i] >= ans[-1]:
        ans.append(srs[i])
        DFS(d + 1)
        ans.pop()
    else:
      ans.append(srs[i])
      DFS(d + 1)
      ans.pop()


DFS(0)
