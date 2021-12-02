import sys
input = sys.stdin.readline
n, m = map(int, input().split())
srs = list(map(int, input().split()))
srs.sort()
ans = []
visited = [0] * n


def DFS(d):
  if d == m:
    print(*ans)
    return

  for i in range(n):
    if not (visited[i]):
      ans.append(srs[i])
      visited[i] = 1
      DFS(d + 1)
      visited[i] = 0
      ans.pop()


DFS(0)
