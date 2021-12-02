import sys
input = sys.stdin.readline
n, m = map(int, input().split())
srs = list(map(int, input().split()))
srs.sort()
ans = []


def DFS(d):
  if d == m:
    print(*ans)
    return

  for i in range(n):
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
